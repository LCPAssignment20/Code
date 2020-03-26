#creating a list
lst = ['Alfa Romeo', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Bugatti', 'Cadillac', 'Chevrolet', 'Chrysler', 'Citroen', 'Corvette','DAF', 'Dacia', 'Daewoo', 'Daihatsu', 'Datsun', 'De Lorean', 'Dino', 'Dodge', 'Farboud', 'Ferrari', 'Ford', 'Honda', 'Hummer', 'Hyundai', 'Jaguar', 'Jeep', 'KIA', 'Koenigsegg', 'Lada', 'Lamborghini', 'Lancia', 'Land Rover', 'Lexus', 'Ligier', 'Lincoln', 'Lotus', 'Martini', 'Maserati', 'Maybach', 'Mazda', 'Mclaren', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Noble', 'Opel', 'Peugot', 'Pontiac', 'Porsche', 'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'Seat', 'Skoda', 'Smart', 'Spyker', 'Subaru', 'Suzuki', 'Toyota', 'Vauxhall', 'Volkswagen', 'Volvo']

n = input("Welcome to Buzzword Bingo! You will now be asked for 10 words that fit the theme Car Brands:")

#opening file and writing in it
with open("Bingo.txt", "w") as myfile:

#loop that asks for 30 words that are appended to the list
    for i in range(0, 10):
        word = (input())

        lst.append(word)

lst = list(dict.fromkeys(lst))

