import paypalrestsdk
import logging

class PayPalPayment:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api = paypalrestsdk.Api({
            'mode': 'sandbox',  # sandbox or live
            'client_id': self.client_id,
            'client_secret': self.client_secret
        })

    def create_payment(self, amount, return_url, cancel_url):
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": return_url,
                "cancel_url": cancel_url
            },
            "transactions": [{
                "amount": {
                    "total": str(amount),
                    "currency": "USD"
                },
                "description": "Payment description"
            }]
        })

        if payment.create():
            print("Payment created successfully")
            for link in payment.links:
                if link.method == "REDIRECT":
                    redirect_url = link.href
                    return redirect_url
        else:
            print(payment.error)
            return None

    def execute_payment(self, payment_id, payer_id):
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            print("Payment executed successfully")
            return True
        else:
            print(payment.error)
            return False

if __name__ == '__main__':
    # Initialize PayPal client
    paypal_client = PayPalPayment('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET')

    # Create a new payment and get the approval URL
    approval_url = paypal_client.create_payment(10, "http://example.com/return", "http://example.com/cancel")
    print(f"Approval URL: {approval_url}")

    # Here you would redirect the user to the approval URL, then they will come back to your return_url
    # At this point, you would take the 'paymentId' and 'PayerID' from the URL parameters and execute the payment

    # Execute the payment (normally this would be done after user approval)
    success = paypal_client.execute_payment('PAYMENT_ID_FROM_URL', 'PAYER_ID_FROM_URL')
    print(f"Payment executed: {success}")
