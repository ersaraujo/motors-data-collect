# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CommTypes.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x43ommTypes.proto\"\x9b\x01\n\rprotoSpeedSSL\x12\n\n\x02vx\x18\x01 \x01(\x01\x12\n\n\x02vy\x18\x02 \x01(\x01\x12\n\n\x02vw\x18\x03 \x01(\x01\x12\r\n\x05\x66ront\x18\x04 \x01(\x08\x12\x0c\n\x04\x63hip\x18\x05 \x01(\x08\x12\x0e\n\x06\x63harge\x18\x06 \x01(\x08\x12\x14\n\x0ckickStrength\x18\x07 \x01(\x01\x12\x10\n\x08\x64ribbler\x18\x08 \x01(\x08\x12\x11\n\tdribSpeed\x18\t \x01(\x01\"\xd0\x01\n\x10protoOdometrySSL\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01w\x18\x03 \x01(\x01\x12\x0f\n\x07hasBall\x18\x04 \x01(\x08\x12\x10\n\x08kickLoad\x18\x05 \x01(\x01\x12\x0f\n\x07\x62\x61ttery\x18\x06 \x01(\x01\x12\r\n\x05\x63ount\x18\x07 \x01(\x05\x12\x10\n\x08vision_x\x18\x08 \x01(\x01\x12\x10\n\x08vision_y\x18\t \x01(\x01\x12\x10\n\x08vision_w\x18\n \x01(\x01\x12\n\n\x02vx\x18\x0b \x01(\x01\x12\n\n\x02vy\x18\x0c \x01(\x01\x12\n\n\x02vw\x18\r \x01(\x01\"\xea\x02\n\x10protoPositionSSL\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01w\x18\x03 \x01(\x01\x12*\n\x07posType\x18\x04 \x01(\x0e\x32\x19.protoPositionSSL.PosType\x12\r\n\x05\x66ront\x18\x05 \x01(\x08\x12\x0c\n\x04\x63hip\x18\x06 \x01(\x08\x12\x0e\n\x06\x63harge\x18\x07 \x01(\x08\x12\x14\n\x0ckickStrength\x18\x08 \x01(\x01\x12\x10\n\x08\x64ribbler\x18\t \x01(\x08\x12\x11\n\tdribSpeed\x18\n \x01(\x01\x12\x15\n\rresetOdometry\x18\x0b \x01(\x08\x12\x11\n\tmin_speed\x18\x0c \x01(\x01\x12\x11\n\tmax_speed\x18\r \x01(\x01\"d\n\x07PosType\x12\x0b\n\x07unknown\x10\x00\x12\n\n\x06source\x10\x01\x12\x08\n\x04stop\x10\x02\x12\x11\n\rdriveToTarget\x10\x03\x12\x10\n\x0crotateOnSelf\x10\x04\x12\x11\n\rrotateInPoint\x10\x05\"C\n\x11protoMotorsPWMSSL\x12\n\n\x02m1\x18\x01 \x01(\x01\x12\n\n\x02m2\x18\x02 \x01(\x01\x12\n\n\x02m3\x18\x03 \x01(\x01\x12\n\n\x02m4\x18\x04 \x01(\x01\"\x85\x02\n\x12protoMotorsDataSSL\x12\x12\n\ncurrent_m1\x18\x01 \x01(\x01\x12\x12\n\ncurrent_m2\x18\x02 \x01(\x01\x12\x12\n\ncurrent_m3\x18\x03 \x01(\x01\x12\x12\n\ncurrent_m4\x18\x04 \x01(\x01\x12\x0e\n\x06pwm_m1\x18\x05 \x01(\x01\x12\x0e\n\x06pwm_m2\x18\x06 \x01(\x01\x12\x0e\n\x06pwm_m3\x18\x07 \x01(\x01\x12\x0e\n\x06pwm_m4\x18\x08 \x01(\x01\x12\x12\n\ndesired_m1\x18\t \x01(\x01\x12\x12\n\ndesired_m2\x18\n \x01(\x01\x12\x12\n\ndesired_m3\x18\x0b \x01(\x01\x12\x12\n\ndesired_m4\x18\x0c \x01(\x01\x12\x0f\n\x07msgTime\x18\r \x01(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CommTypes_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PROTOSPEEDSSL']._serialized_start=20
  _globals['_PROTOSPEEDSSL']._serialized_end=175
  _globals['_PROTOODOMETRYSSL']._serialized_start=178
  _globals['_PROTOODOMETRYSSL']._serialized_end=386
  _globals['_PROTOPOSITIONSSL']._serialized_start=389
  _globals['_PROTOPOSITIONSSL']._serialized_end=751
  _globals['_PROTOPOSITIONSSL_POSTYPE']._serialized_start=651
  _globals['_PROTOPOSITIONSSL_POSTYPE']._serialized_end=751
  _globals['_PROTOMOTORSPWMSSL']._serialized_start=753
  _globals['_PROTOMOTORSPWMSSL']._serialized_end=820
  _globals['_PROTOMOTORSDATASSL']._serialized_start=823
  _globals['_PROTOMOTORSDATASSL']._serialized_end=1084
# @@protoc_insertion_point(module_scope)
