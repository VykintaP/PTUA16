CURRENT_YEAR = 2024


class ElectronicDevice:
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        password: str = "manager123",
    ):
        self._brand: str = brand
        self._price: float = price
        self._warranty_period: int = warranty_period
        self._stock: int = stock
        self._store_password: str = password
        self._discount: int = 0
        self._is_discount_applied: bool = False

    def get_details(self) -> str:
        return (
            f"Prekės ženklas: {self._brand}, Kaina: {self._price:.2f} €, Garantija: "
            f"{self._warranty_period} metai, Atsargos: {self._stock} vienetai"
        )

    def purchase(self) -> None:
        if self._stock > 0:
            self._stock -= 1
            print(f"Įrenginys nupirktas! Liko atsargų: {self._stock}")
        else:
            print("Šios prekės nėra sandėlyje!")

    def restock(self, quantity: int, password: str) -> None:
        if password == self._store_password:
            self._stock += quantity
            print(
                f"Atsargos papildytos {quantity} vienetais. Naujos atsargos: "
                f"{self._stock}"
            )
        else:
            print("Neteisėta prieiga: neteisingas slaptažodis.")

    def _is_warranty_valid(self, year_of_purchase: int) -> bool:
        return CURRENT_YEAR - year_of_purchase <= self._warranty_period

    def return_device(self, year_of_purchase: int) -> None:
        if self._is_warranty_valid(year_of_purchase):
            self._stock += 1
            print(f"Įrenginys sėkmingai grąžintas! Atsargos atnaujintos: {self._stock}")
        else:
            print("Garantija pasibaigusi. Įrenginio grąžinti negalima.")

    def apply_discount(self, discount: int = None) -> None:
        if self._is_discount_applied:
            print("Nuolaida jau pritaikyta.")
        else:
            if discount is None:
                discount = self._discount
            self._price = round(self._price * (1 - discount / 100), 2)
            self._is_discount_applied = True
            print(f"Nuolaida {discount} % pritaikyta. Nauja kaina: {self._price:.2f} €")


class Laptop(ElectronicDevice):
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        ram: int,
        storage: int,
        password: str = "manager123",
    ):
        super().__init__(brand, price, warranty_period, stock, password)
        self._ram = ram
        self._storage = storage
        self._discount = 5

    def get_details(self) -> str:
        return (
            super().get_details() + f", RAM: {self._ram} GB, Atmintis: "
            f"{self._storage} GB"
        )

    def upgrade_ram(self, new_ram: int) -> None:
        if new_ram > self._ram:
            self._ram = new_ram
            print(f"RAM atmintis sėkmingai atnaujinta iki {self._ram} GB.")
        else:
            print("Nauja RAM atminties reikšmė turi būti didesnė už dabartinę.")


class Smartphone(ElectronicDevice):
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        screen_size: float,
        battery_capacity: int,
        password: str = "manager123",
    ):
        super().__init__(brand, price, warranty_period, stock, password)
        self._screen_size = screen_size
        self._battery_capacity = battery_capacity
        self._discount = 3

    def get_details(self) -> str:
        return (
            super().get_details()
            + f", Ekrano dydis: {self._screen_size} colių, Baterija: {self._battery_capacity} mAh"
        )

    def upgrade_battery(self, new_battery_capacity: int) -> None:
        if new_battery_capacity > self._battery_capacity:
            self._battery_capacity = new_battery_capacity
            print(f"Baterija atnaujinta iki {self._battery_capacity} mAh.")
        else:
            print("Nauja baterijos talpa turi būti didesnė už dabartinę.")


class Television(ElectronicDevice):
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        screen_size: float,
        resolution: str,
        password: str = "manager123",
    ):
        super().__init__(brand, price, warranty_period, stock, password)
        self._screen_size = screen_size
        self._resolution = resolution
        self._discount = 10

    def get_details(self) -> str:
        return (
            super().get_details()
            + f", Ekrano dydis: {self._screen_size} colių, Raiška: {self._resolution}"
        )

    def upgrade_resolution(self, new_resolution: str) -> None:
        if new_resolution != self._resolution:
            self._resolution = new_resolution
            print(f"Raiška atnaujinta iki {self._resolution}.")
        else:
            print("Nauja raiška turi skirtis nuo dabartinės.")

# Sukuriame objektus
laptop = Laptop("Dell", 1200.00, 3, 10, ram=16, storage=512)
smartphone = Smartphone("iPhone", 999.99, 2, 20, screen_size=6.1, battery_capacity=4000)
television = Television("Samsung", 1500.00, 5, 5, screen_size=55, resolution="4K")

# Detalės
print(laptop.get_details())
print(smartphone.get_details())
print(television.get_details())

# Nuolaidų taikymas
laptop.apply_discount()  # Nuolaida 5%
smartphone.apply_discount()  # Nuolaida 3%
television.apply_discount()  # Nuolaida 10%

# Pirkimas
laptop.purchase()
smartphone.purchase()
television.purchase()

# Atsargų papildymas
television.restock(5, "wrong_password")  # Klaidingas slaptažodis
television.restock(5, "manager123")  # Teisingas slaptažodis

# Atributų atnaujinimas
laptop.upgrade_ram(32)
smartphone.upgrade_battery(5000)
television.upgrade_resolution("8K")
