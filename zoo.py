class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: # Fix correct condition
            return 50
        elif 13 <= age < 20:
            return 100
        elif 21 <= age <= 60: # Fix correct condition
            return 150
        elif age > 60: # Fix correct condition
            return 100