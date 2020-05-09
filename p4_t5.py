class Soldier():
    def __init__(self):
        pass

    def action(self, name, act):
        print(f'Soldier has an {name} and fires {act}')

class Guns():
    def __init__(self):
        pass

    def fire_reload(self, bullets, fill=0):
        if bullets <= 40:
            bullets =  40 - bullets
        print(f'Left: {bullets}')

        bullets += fill
        print(f'Reloaded to: {bullets}')   #'AK47', "'tigi-tigitishh'"

class Act_of_Shooting(Soldier, Guns):
    pass

act = Act_of_Shooting()
act.action('AK47', "'tigi-tigitishh'")
act.fire_reload(30, 10)
