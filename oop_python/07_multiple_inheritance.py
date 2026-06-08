"""Multiple inheritance example."""


class Camera:
    def take_photo(self):
        return "Taking a photo."


class Phone:
    def make_call(self):
        return "Making a phone call."


class SmartPhone(Camera, Phone):
    # SmartPhone gets methods from both Camera and Phone.
    def browse_internet(self):
        return "Browsing the internet."


mobile = SmartPhone()

print(mobile.take_photo())
print(mobile.make_call())
print(mobile.browse_internet())
