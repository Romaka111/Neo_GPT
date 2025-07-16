# app/webhook/yoomoney.py

from fastapi import APIRouter, Request, Response, status
from app.core.payment import process_payment

router = APIRouter()

@router.post("/yoomoney/webhook")
async def yoomoney_webhook(request: Request):
    """
    Получает уведомления от ЮMoney.
    """
    form = await request.form()
    data = dict(form)

    try:
        await process_payment(data)
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:
        print(f"Ошибка при обработке платежа: {e}")
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
