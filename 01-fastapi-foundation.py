from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title = "Swiggy Order Service",
    description = (
        "Internal API for managing orders"
        "Hanlde creation, tracking of delivery systems"
    ),
    version = "1.2.1",
    docs_url = "/docs",
    redoc_url = "/redoc", # Fancy doc version
    openapi_url = "/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint - Health Check"""
    # FastAPI converts this dict in json
    return {"messagge": "Welcome to Swiggy Order Service", "status": "healthy"}

print(read_root.__doc__)

@app.get("/about")
def about():
    """Returns API Meta Data"""
    return {
        "service": "order-service",
        "team": "backend platform",
        "region": "ap-south-1",
        "version": "1.2.2"
    }

@app.get("/orders")
def list_orders():
    """List Recent Orders"""
    return {
        "orders": [
            {"id": "1", "item": "Butter Chicken", "status": "delivered"},
            {"id": "2", "item": "Chicken Samosa", "status": "delivered"},
            {"id": "3", "item": "Biryani", "status": "delivered"},
        ]
    }
    
@app.get("/orders/status")
def order_status():
    """Get Order Status"""
    return {
        "total_today": 2_340_23,
        "top_city": "Bangaluru"
    }
    
@app.get("/debug/request-info")
async def request_info(request: Request):
    """Inspect the raw request object"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }
    
@app.get(
    "/orders/active",
    summary = "Get Active Orders",
    description = (
        "Returns all orders that are currently being prepared "
        "or are out for delivery"
    ),
    tags = ["Orders"],
    response_description = "List of active order objects",
    deprecated = False
)
def get_active_order():
    """This docstring also appears in docs"""
    return {
        "active_orders": [
            {"id": 1, "item": "Biyani", "status": "out_for_delivery"}
        ]
    }
    
@app.get("/restaurants", tags = ["Restaurants"])
def list_restro():
    """another docstring for another endpoint"""
    return {
        "restaurants": [
            {"test": "test"}
        ]
    }
    
@app.get("/restaurants/delhi", tags = ["Restaurants"])
def list_restro():
    """another docstring for another endpoint"""
    return {
        "restaurants": [
            {"test": "test"}
        ]
    }