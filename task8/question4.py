class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = None  # Add any default price if needed
        self.inches = None  # Add any default inches if needed
        self.on = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = None  # Add default value if needed
        self.backlight = None  # Add default value if needed

    def display_details(self):
        return f"{self.brand} LED TV\nScreen Thickness: {self.screen_thickness}\nEnergy Usage: {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate}\nViewing Angle: {self.viewing_angle}\nBacklight: {self.backlight}"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        return f"{self.brand} Plasma TV\nScreen Thickness: {self.screen_thickness}\nEnergy Usage: {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate}"
