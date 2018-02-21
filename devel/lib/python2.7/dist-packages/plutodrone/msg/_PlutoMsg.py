# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from plutodrone/PlutoMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PlutoMsg(genpy.Message):
  _md5sum = "7dc4340a5f0f0b90461e5b4bfba1b568"
  _type = "plutodrone/PlutoMsg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int64 rcRoll
int64 rcPitch
int64 rcYaw
int64 rcThrottle
int64 rcAUX1
int64 rcAUX2
int64 rcAUX3
int64 rcAUX4

"""
  __slots__ = ['rcRoll','rcPitch','rcYaw','rcThrottle','rcAUX1','rcAUX2','rcAUX3','rcAUX4']
  _slot_types = ['int64','int64','int64','int64','int64','int64','int64','int64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       rcRoll,rcPitch,rcYaw,rcThrottle,rcAUX1,rcAUX2,rcAUX3,rcAUX4

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlutoMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.rcRoll is None:
        self.rcRoll = 0
      if self.rcPitch is None:
        self.rcPitch = 0
      if self.rcYaw is None:
        self.rcYaw = 0
      if self.rcThrottle is None:
        self.rcThrottle = 0
      if self.rcAUX1 is None:
        self.rcAUX1 = 0
      if self.rcAUX2 is None:
        self.rcAUX2 = 0
      if self.rcAUX3 is None:
        self.rcAUX3 = 0
      if self.rcAUX4 is None:
        self.rcAUX4 = 0
    else:
      self.rcRoll = 0
      self.rcPitch = 0
      self.rcYaw = 0
      self.rcThrottle = 0
      self.rcAUX1 = 0
      self.rcAUX2 = 0
      self.rcAUX3 = 0
      self.rcAUX4 = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_8q.pack(_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4,) = _struct_8q.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_8q.pack(_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 64
      (_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4,) = _struct_8q.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_8q = struct.Struct("<8q")
