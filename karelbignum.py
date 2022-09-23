from stanfordkarel import *

class ktools:
  def m(self):
    """Shorthand for move"""
    move()
  def tl(self):
    """Turn Left"""
    turn_left()
  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl ()
  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()
  def pick(self):
    """Pick Beeper"""
    pick_beeper()
  def put(self):
    """Put Beeper"""
    put_beeper()
  def put2(self):
    """Put two beepers in row"""
    self.put()
    self.m()
    self.put()
  def put5(self):
    """Put five beepers in a row"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()
  def put4(self):
    self.put2()
    self.m()
    self.put2()
  def m5(self):
    self.m()
    self.m()
    self.m()
    self.m()
    self.m()
  def O(self):
    self.put4()
    self.tl()
    self.m()
    self.put4()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.put()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.put()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m5()
  
    
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.tl()
    kt.put5()
    kt.ta()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.O()
    kt.O()
    kt.O()
    kt.O()
    kt.O()
    kt.O()
    kt.O()
    kt.O()
    kt.O()
    
    pass


if __name__ == "__main__":
    run_karel_program()