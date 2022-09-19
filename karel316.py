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
  def pick3(self):
    self.pick()
    self.m()
    self.pick()
    self.m()
    self.pick()
  def pickbox(self):
    self.pick3()
    self.tl()
    self.m()
    self.pick3()
    self.tl()
    self.m()
    self.pick3()
    self.tl()
    self.m()
    self.pick3()
    self.tl()
  
    
def main():
    """ Karel code goes here! """
    kt=ktools()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.pickbox()
    
    pass


if __name__ == "__main__":
    run_karel_program()