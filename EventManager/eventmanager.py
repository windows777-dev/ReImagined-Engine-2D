from pyray import *

class EventManager:

    def __init__(self, max_events=-1):
        self.max_events=max_events
        self.events = []
        self.fired_events = [] # Fired events are put in here, if not handled after 30s it gets destroyed

    def register_event(self, event):
        self.events.append(event)

    def invoked(self, event_name):
        is_invoked = next((obj for obj in self.fired_events if obj.name == event_name), None)
        if is_invoked != None:
            self.fired_events.remove(is_invoked)
            return True
        else:
            return False
        

    def update(self):

        self.events = [e for e in self.events if e.life_time <= 30.0]

        for event in self.events:
            event.life_time += get_frame_time()
            if event.invoked:
                self.fired_events.append(event)
                event.invoked = False