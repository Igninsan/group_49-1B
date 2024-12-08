class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print(f'Memory * cpu: {self.__memory * self.__cpu}')

    def __str__(self):
        return f'Cpu: {self.__cpu}, memory: {self.__memory} '

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_card(self):
        return self.__sim_cards_list


    @sim_card.setter
    def sim_card(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number} - {self.__sim_cards_list[sim_card_number - 1]}')

    def __str__(self):
        return f'List of sim cards: {self.__sim_cards_list}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        self.__sim_cards_list = sim_cards_list

    def use_gps(self, location):
        print(f'Построен путь до локации {location}')

    def __str__(self):
        return super().__str__() + f', List of sim cards: {self.__sim_cards_list}'

comp_1 = Computer(4010, 8192)
phone_1 = Phone(['MegaCom', 'O!'])
smartphone_1 = SmartPhone(1000, 1024, ['Beeline', 'Megacom'])
smartphone_2 = SmartPhone(2000, 2048, ['O!'])

gadget_list = [comp_1, phone_1, smartphone_1, smartphone_2]

for gadget in gadget_list:
    print(gadget)

print()

comp_1.make_computations()
phone_1.call(1, '+996 532 36 32 60')
smartphone_1.use_gps('Bishkek Park')

print()

print(smartphone_1 > smartphone_2)
print(smartphone_1 < smartphone_2)
print(smartphone_1 == smartphone_2)
print(smartphone_1 != smartphone_2)
print(smartphone_1 >= smartphone_2)
print(smartphone_1 <= smartphone_2)
