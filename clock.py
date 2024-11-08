import time

class Clock:

    def set_hours(this, h):
        if not (0 <= h < 24):
            raise ValueError(f"Invalid value for hours: {h}")
        this.hours = h

    def set_minutes(this, m):
        if not (0 <= m < 60): 
            raise ValueError(f"Invalid value for minutes: {m}")
        this.minutes = m

    def set_seconds(this, s):
        if not (0 <= s < 60):
            raise ValueError(f"Invalid value for seconds: {s}")
        this.seconds = s

    def __init__(this,h,m,s):
        this.set_hours(h)
        this.set_minutes(m)
        this.set_seconds(s)

    def __str__(this):
        return f"{this.hours:02}:{this.minutes:02}:{this.seconds:02}"

    def tick(this):
        if this.seconds == 59:
            this.seconds = 0
            if this.minutes == 59:
                this.minutes = 0
                if this.hours == 23:
                    this.hours = 0
                else:
                    this.hours += 1
            else:
                this.minutes += 1
        else:
            this.seconds += 1
    
    def run(this):
        while True:
            print(str(this))
            time.sleep(1)
            this.tick()
