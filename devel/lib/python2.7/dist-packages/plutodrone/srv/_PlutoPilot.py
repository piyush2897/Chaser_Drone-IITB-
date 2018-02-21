# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from plutodrone/PlutoPilotRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PlutoPilotRequest(genpy.Message):
  _md5sum = "4e61791776d560375085144e1668140e"
  _type = "plutodrone/PlutoPilotRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

int32 roll
int32 pitch
int32 yaw
float32 accX
float32 accY
float32 accZ
float32 gyroX
float32 gyroY
float32 gyroZ
float32 magX
float32 magY
float32 magZ
float32 alt

"""
  __slots__ = ['roll','pitch','yaw','accX','accY','accZ','gyroX','gyroY','gyroZ','magX','magY','magZ','alt']
  _slot_types = ['int32','int32','int32','float32','float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       roll,pitch,yaw,accX,accY,accZ,gyroX,gyroY,gyroZ,magX,magY,magZ,alt

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlutoPilotRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.roll is None:
        self.roll = 0
      if self.pitch is None:
        self.pitch = 0
      if self.yaw is None:
        self.yaw = 0
      if self.accX is None:
        self.accX = 0.
      if self.accY is None:
        self.accY = 0.
      if self.accZ is None:
        self.accZ = 0.
      if self.gyroX is None:
        self.gyroX = 0.
      if self.gyroY is None:
        self.gyroY = 0.
      if self.gyroZ is None:
        self.gyroZ = 0.
      if self.magX is None:
        self.magX = 0.
      if self.magY is None:
        self.magY = 0.
      if self.magZ is None:
        self.magZ = 0.
      if self.alt is None:
        self.alt = 0.
    else:
      self.roll = 0
      self.pitch = 0
      self.yaw = 0
      self.accX = 0.
      self.accY = 0.
      self.accZ = 0.
      self.gyroX = 0.
      self.gyroY = 0.
      self.gyroZ = 0.
      self.magX = 0.
      self.magY = 0.
      self.magZ = 0.
      self.alt = 0.

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
      buff.write(_struct_3i10f.pack(_x.roll, _x.pitch, _x.yaw, _x.accX, _x.accY, _x.accZ, _x.gyroX, _x.gyroY, _x.gyroZ, _x.magX, _x.magY, _x.magZ, _x.alt))
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
      end += 52
      (_x.roll, _x.pitch, _x.yaw, _x.accX, _x.accY, _x.accZ, _x.gyroX, _x.gyroY, _x.gyroZ, _x.magX, _x.magY, _x.magZ, _x.alt,) = _struct_3i10f.unpack(str[start:end])
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
      buff.write(_struct_3i10f.pack(_x.roll, _x.pitch, _x.yaw, _x.accX, _x.accY, _x.accZ, _x.gyroX, _x.gyroY, _x.gyroZ, _x.magX, _x.magY, _x.magZ, _x.alt))
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
      end += 52
      (_x.roll, _x.pitch, _x.yaw, _x.accX, _x.accY, _x.accZ, _x.gyroX, _x.gyroY, _x.gyroZ, _x.magX, _x.magY, _x.magZ, _x.alt,) = _struct_3i10f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3i10f = struct.Struct("<3i10f")
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from plutodrone/PlutoPilotResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PlutoPilotResponse(genpy.Message):
  _md5sum = "c7a7b135453cda7e71490802dabf7edd"
  _type = "plutodrone/PlutoPilotResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

int32 rcRoll
int32 rcPitch
int32 rcYaw
int32 rcThrottle
int32 rcAUX1
int32 rcAUX2
int32 rcAUX3
int32 rcAUX4

"""
  __slots__ = ['rcRoll','rcPitch','rcYaw','rcThrottle','rcAUX1','rcAUX2','rcAUX3','rcAUX4']
  _slot_types = ['int32','int32','int32','int32','int32','int32','int32','int32']

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
      super(PlutoPilotResponse, self).__init__(*args, **kwds)
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
      buff.write(_struct_8i.pack(_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4))
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
      end += 32
      (_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4,) = _struct_8i.unpack(str[start:end])
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
      buff.write(_struct_8i.pack(_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4))
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
      end += 32
      (_x.rcRoll, _x.rcPitch, _x.rcYaw, _x.rcThrottle, _x.rcAUX1, _x.rcAUX2, _x.rcAUX3, _x.rcAUX4,) = _struct_8i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_8i = struct.Struct("<8i")
class PlutoPilot(object):
  _type          = 'plutodrone/PlutoPilot'
  _md5sum = 'a9cb76ac323ce16acce1b8357e8cbb55'
  _request_class  = PlutoPilotRequest
  _response_class = PlutoPilotResponse
