# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from proto import param_pb2 as proto_dot_param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10proto/task.proto\x12\x1d\x63om.mimikko.app.api.play.task\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x11proto/param.proto\"M\n\x07request\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0c\x66orceRefresh\x18\x02 \x01(\x08\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x10\n\x08pageSize\x18\x04 \x01(\x05\"w\n\x08response\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\x12<\n\x07\x63ontent\x18\x04 \x03(\x0b\x32+.com.mimikko.app.api.play.task.GetTaskReply\"\xb2\x05\n\x0cGetTaskReply\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08recordId\x18\x03 \x01(\x03\x12\x0e\n\x06poster\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x14\n\x0c\x64urationDesc\x18\x06 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x07 \x01(\t\x12\x17\n\x0f\x66inishCondition\x18\x08 \x01(\t\x12:\n\x06status\x18\t \x01(\x0e\x32*.com.mimikko.app.api.play.param.PlayStatus\x12L\n\x10\x63haractersRecord\x18\n \x01(\x0b\x32\x32.com.mimikko.app.api.play.param.PlayCharacterReply\x12\x1b\n\x13\x63haracterLimitUpper\x18\x0b \x01(\x05\x12\x16\n\x0e\x63haracterLimit\x18\x0c \x01(\t\x12H\n\x10\x63haracterRewards\x18\r \x01(\x0b\x32..com.mimikko.app.api.play.task.CharacterReward\x12\x30\n\x0c\x63ompleteTime\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rremainingTime\x18\x0f \x01(\x05\x12\x10\n\x08sendName\x18\x10 \x01(\t\x12\x0e\n\x06\x62\x61nner\x18\x11 \x01(\t\x12\r\n\x05level\x18\x12 \x01(\t\x12\x12\n\nbackground\x18\x13 \x01(\t\x12W\n\x17taskRewardMagnification\x18\x14 \x01(\x0b\x32\x36.com.mimikko.app.api.play.task.TaskRewardMagnification\x12+\n\x07sysTime\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x88\x01\n\x0f\x43haracterReward\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x63over\x18\x03 \x01(\t\x12J\n\x07rewards\x18\x04 \x01(\x0b\x32\x39.com.mimikko.app.api.play.param.MaterialScalarDetailReply\"\x16\n\x08request2\x12\n\n\x02id\x18\x01 \x01(\x03\"\xaf\x05\n\tresponse2\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08recordId\x18\x03 \x01(\x03\x12\x0e\n\x06poster\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x14\n\x0c\x64urationDesc\x18\x06 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x07 \x01(\t\x12\x17\n\x0f\x66inishCondition\x18\x08 \x01(\t\x12:\n\x06status\x18\t \x01(\x0e\x32*.com.mimikko.app.api.play.param.PlayStatus\x12L\n\x10\x63haractersRecord\x18\n \x01(\x0b\x32\x32.com.mimikko.app.api.play.param.PlayCharacterReply\x12\x1b\n\x13\x63haracterLimitUpper\x18\x0b \x01(\x05\x12\x16\n\x0e\x63haracterLimit\x18\x0c \x01(\t\x12H\n\x10\x63haracterRewards\x18\r \x01(\x0b\x32..com.mimikko.app.api.play.task.CharacterReward\x12\x30\n\x0c\x63ompleteTime\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rremainingTime\x18\x0f \x01(\x05\x12\x10\n\x08sendName\x18\x10 \x01(\t\x12\x0e\n\x06\x62\x61nner\x18\x11 \x01(\t\x12\r\n\x05level\x18\x12 \x01(\t\x12\x12\n\nbackground\x18\x13 \x01(\t\x12W\n\x17taskRewardMagnification\x18\x14 \x01(\x0b\x32\x36.com.mimikko.app.api.play.task.TaskRewardMagnification\x12+\n\x07sysTime\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc7\x01\n\x17TaskRewardMagnification\x12T\n\x07mapdata\x18\x01 \x03(\x0b\x32\x43.com.mimikko.app.api.play.task.TaskRewardMagnification.MapdataEntry\x1aV\n\x0cMapdataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.com.mimikko.app.api.play.task.MapData:\x02\x38\x01\"\x15\n\x07MapData\x12\n\n\x02s3\x18\x03 \x01(\t\"J\n\x08request3\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\ncodesLimit\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x10\n\x08pageSize\x18\x04 \x01(\x05\"\x7f\n\tresponse3\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\x12\x43\n\x07\x63ontent\x18\x04 \x03(\x0b\x32\x32.com.mimikko.app.api.play.param.PlayCharacterReply\"\x16\n\x08request4\x12\n\n\x02id\x18\x01 \x01(\x03\"\xa6\x01\n\tresponse4\x12J\n\x07rewards\x18\x01 \x01(\x0b\x32\x39.com.mimikko.app.api.play.param.MaterialScalarDetailReply\x12M\n\npost_cards\x18\x02 \x01(\x0b\x32\x39.com.mimikko.app.api.play.param.MaterialScalarDetailReply\"X\n\x08request5\x12\n\n\x02id\x18\x01 \x01(\x03\x12@\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x32.com.mimikko.app.api.play.task.PickTaskRequestBody\",\n\x13PickTaskRequestBody\x12\x15\n\rcharacterCode\x18\x01 \x01(\t\"\x1a\n\tresponse5\x12\r\n\x05value\x18\x01 \x01(\t2\x80\x04\n\x04Task\x12]\n\x08ListTask\x12&.com.mimikko.app.api.play.task.request\x1a\'.com.mimikko.app.api.play.task.response\"\x00\x12\x64\n\rGetTaskRecord\x12\'.com.mimikko.app.api.play.task.request2\x1a(.com.mimikko.app.api.play.task.response2\"\x00\x12h\n\x11ListTaskCharacter\x12\'.com.mimikko.app.api.play.task.request3\x1a(.com.mimikko.app.api.play.task.response3\"\x00\x12h\n\x11ReceiveTaskReward\x12\'.com.mimikko.app.api.play.task.request4\x1a(.com.mimikko.app.api.play.task.response4\"\x00\x12_\n\x08PickTask\x12\'.com.mimikko.app.api.play.task.request5\x1a(.com.mimikko.app.api.play.task.response5\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TASKREWARDMAGNIFICATION_MAPDATAENTRY._options = None
  _TASKREWARDMAGNIFICATION_MAPDATAENTRY._serialized_options = b'8\001'
  _REQUEST._serialized_start=103
  _REQUEST._serialized_end=180
  _RESPONSE._serialized_start=182
  _RESPONSE._serialized_end=301
  _GETTASKREPLY._serialized_start=304
  _GETTASKREPLY._serialized_end=994
  _CHARACTERREWARD._serialized_start=997
  _CHARACTERREWARD._serialized_end=1133
  _REQUEST2._serialized_start=1135
  _REQUEST2._serialized_end=1157
  _RESPONSE2._serialized_start=1160
  _RESPONSE2._serialized_end=1847
  _TASKREWARDMAGNIFICATION._serialized_start=1850
  _TASKREWARDMAGNIFICATION._serialized_end=2049
  _TASKREWARDMAGNIFICATION_MAPDATAENTRY._serialized_start=1963
  _TASKREWARDMAGNIFICATION_MAPDATAENTRY._serialized_end=2049
  _MAPDATA._serialized_start=2051
  _MAPDATA._serialized_end=2072
  _REQUEST3._serialized_start=2074
  _REQUEST3._serialized_end=2148
  _RESPONSE3._serialized_start=2150
  _RESPONSE3._serialized_end=2277
  _REQUEST4._serialized_start=2279
  _REQUEST4._serialized_end=2301
  _RESPONSE4._serialized_start=2304
  _RESPONSE4._serialized_end=2470
  _REQUEST5._serialized_start=2472
  _REQUEST5._serialized_end=2560
  _PICKTASKREQUESTBODY._serialized_start=2562
  _PICKTASKREQUESTBODY._serialized_end=2606
  _RESPONSE5._serialized_start=2608
  _RESPONSE5._serialized_end=2634
  _TASK._serialized_start=2637
  _TASK._serialized_end=3149
# @@protoc_insertion_point(module_scope)