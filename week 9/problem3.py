#(Medium): Cargo Crate
#A CargoCrate has fields: crate_id (str), destination (str), max_weight (float), and items which starts as an empty list of (name, weight) tuples.

from dataclasses import dataclass, field

@dataclass
class CargoCrate:
    crate_id: str
    destination: str
    max_weight: float
    #items: list = field(default_factory=list[tuple) #empty list of (name, weight) tuples.
    items: list[tuple[str, float]] = field(default_factory=list)

#total_weight(self) -> float — returns the combined weight of all items in the crate.

    def total_weight(self)-> float:
        return sum(item[1] for item in self.items)

#add_item(self, name: str, weight: float) -> bool — adds the item only if doing so would not exceed the crate’s weight limit. Returns whether the item was successfully added.

    def add_item(self, name: str, weight: float) -> bool:
        if self.total_weight() + weight > self.max_weight:
            return False
        self.items.append((name, weight))
        return True
#manifest(self) — prints a formatted summary of the crate. Study the expected output to determine the exact format.
#Crate CR-401 -> Arrakis
#  - Stillsuit: 8.5kg
#  - Spice Melange: 30.0kg
#Total: 38.5/50.0kg

    def manifest(self):
        print(f"Crate {self.crate_id} -> {self.destination}")
        for name, weight in self.items:
            print(f"  -{name}: {weight}kg") 
        print(f"Total: {self.total_weight()}/{self.max_weight}")

c = CargoCrate("CR-401", "Arrakis", 50.0)
print(c.add_item("Stillsuit", 8.5))
print(c.add_item("Spice Melange", 30.0))
print(c.add_item("Shield Generator", 15.0))
print(c.total_weight())
c.manifest()