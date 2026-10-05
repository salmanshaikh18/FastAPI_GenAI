from fastapi import FastAPI
from exceptions import (
    PinCodeNotFoundError,
    pincode_not_found_handler,
    InvalidPinCodeError,
    invalid_pincode_handler
)
from models import LocationResponse, BulkRequest, BulkResponse
from data import pincode_db

app = FastAPI(
    title = "Pincode Lookup API",
    description = "Auto fill city and state from Indian Pincode during checkout"
)

# register custom exception handler
app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)

@app.get("/")
def root():
    return {
        "message": "Pincode Lookup API"
    }
    
@app.get("/pincode/{pincode}", response_model = LocationResponse)
def lookup_pincode(pincode: str):
    if len(pincode) != 6 or not pincode.isdigit():
        raise InvalidPinCodeError(pincode, "Must be exactly 6 digit")
    
    if pincode not in pincode_db:
        raise PinCodeNotFoundError(pincode)
    return pincode_db[pincode]


@app.post("/pincode/bulk", response_model = BulkResponse)
def bulk_lookup(request: BulkRequest):
    results = []
    missing = []
    
    for pincode in request.pincodes:
        if pincode in pincode_db:
            results.append(pincode_db[pincode])
        else: 
            missing.append(pincode)
            
    return BulkResponse(
        found = len(results),
        not_found = len(missing),
        results = results,
        missing = missing
    )
