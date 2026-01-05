from fastapi import FastAPI
from app.schema import TicketRequest, TicketResponse
from app.model import predict_priority
from app.database import get_db

app = FastAPI(title="AI Email Priority Classifier")

@app.post("/classify", response_model=TicketResponse)
def classify_ticket(ticket: TicketRequest):
    priority = predict_priority(ticket.message)

    db = get_db()
    db.execute(
        "INSERT INTO tickets (message, priority) VALUES (?, ?)",
        (ticket.message, priority)
    )
    db.commit()
    db.close()

    return {"priority": priority}
