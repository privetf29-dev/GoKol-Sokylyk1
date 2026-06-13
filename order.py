from aiogram.fsm.state import State, StatesGroup

class OrderState(StatesGroup):
    service = State()
    from_address = State()
    to_address = State()
    details = State()
    phone = State()
