


from enum import Enum


class SystemStatuses(Enum):
    EXCELLENT = 0
    GOOD = 1
    AVERAGE = 2
    DEGRADED = 3
    POOR = 4
class TyreStatus(SystemStatuses):
    pass
class PetrolCombustionSystemStatus(SystemStatuses):
    pass

class FuelTypes(Enum):
    DIESEL = 0
    PETROL = 1
    NATURAL = 2
    LPG = 3
    ELECTRICITY = 4
    NONE = 5


class Engine(object):
    fuel_type = FuelTypes.NONE
    def __init__(self, fuel_type) -> None:
        if not isinstance(fuel_type, FuelTypes):
            raise ValueError("fuel_type must be of the FuelTypes enum.")
        fuel_type = fuel_type
    

class PetrolEngine(Engine):
    combustion_system_status = PetrolCombustionSystemStatus.POOR
    fuel_consumption_rate = 1
    fuel_loss_rate = 0
    fuel_consumption_per_km = 0
    def __init__(self, fuel_type) -> None:
        super().__init__(fuel_type)


    

class Carriage(object):
    fuel = FuelTypes.NONE

    def __init__(self) -> None:
        pass

class Car(Carriage):
    engine = PetrolEngine(FuelTypes.PETROL)
    def __init__(self, fuel_type) -> None:

    def compute_consumption():
        pass

    def set_fuel_level():
        pass
    def get_fuel_level():
        pass
    def set_tyre_status(status):
        pass
    def get_tyre_status() -> TyreStatus:
        pass


class CarriageWay(object):
    def __init__(self) -> None:
        pass

class Road(CarriageWay):
    def __init__(self) -> None:
        super().__init__()

class Motorway(CarriageWay):
    def __init__(self) -> None:
        super().__init__()
