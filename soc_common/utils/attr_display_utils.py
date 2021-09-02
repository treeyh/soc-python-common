

class AttrDisplay:
  def gatherAttrs(self):
    return ",".join("{}={}"
                    .format(k, getattr(self, k))
                    for k in self.__dict__.keys())

  def __repr__(self):
    return "{{{}:{}}}".format(self.__class__.__name__, self.gatherAttrs())
