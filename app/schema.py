from pydantic import BaseModel

class TicketRequest(BaseModel):
    message: str

class TicketResponse(BaseModel):
    priority: str
