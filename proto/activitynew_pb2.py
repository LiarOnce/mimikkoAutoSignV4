# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/activitynew.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17proto/activitynew.proto\x12$com.mimikko.app.api.daylife.activity\"J\n\x16ListActivityNewRequest\x12\x10\n\x08typeCode\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x05 \x01(\x05\x12\x10\n\x08pageSize\x18\x06 \x01(\x05\"\x94\x01\n\x17ListActivityNewResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12J\n\x07\x63ontent\x18\x04 \x03(\x0b\x32\x39.com.mimikko.app.api.daylife.activity.GetActivityNewReply\"\xfe\x01\n\x13GetActivityNewReply\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x63over\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x12\n\nurlUseType\x18\x06 \x01(\x05\x12\x0c\n\x04info\x18\x07 \x01(\t\x12\x10\n\x08typeCode\x18\x08 \x01(\t\x12\x10\n\x08typeName\x18\t \x01(\t\x12\x10\n\x08\x65ndpoint\x18\n \x01(\t\x12\x12\n\ncreateTime\x18\x0b \x01(\x03\x12\x13\n\x0btodaySigned\x18\x0c \x01(\x08\x12\x11\n\tstartTime\x18\r \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x0e \x01(\x03\"\x1e\n\x1cGetTodayAvailableSignRequest\"0\n\x1dGetTodayAvailableSignResponse\x12\x0f\n\x03ids\x18\x01 \x03(\x03\x42\x02\x10\x01\x32\xc5\x02\n\x0b\x41\x63tivityNew\x12\x90\x01\n\x0fListActivityNew\x12<.com.mimikko.app.api.daylife.activity.ListActivityNewRequest\x1a=.com.mimikko.app.api.daylife.activity.ListActivityNewResponse\"\x00\x12\xa2\x01\n\x15GetTodayAvailableSign\x12\x42.com.mimikko.app.api.daylife.activity.GetTodayAvailableSignRequest\x1a\x43.com.mimikko.app.api.daylife.activity.GetTodayAvailableSignResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.activitynew_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETTODAYAVAILABLESIGNRESPONSE.fields_by_name['ids']._options = None
  _GETTODAYAVAILABLESIGNRESPONSE.fields_by_name['ids']._serialized_options = b'\020\001'
  _LISTACTIVITYNEWREQUEST._serialized_start=65
  _LISTACTIVITYNEWREQUEST._serialized_end=139
  _LISTACTIVITYNEWRESPONSE._serialized_start=142
  _LISTACTIVITYNEWRESPONSE._serialized_end=290
  _GETACTIVITYNEWREPLY._serialized_start=293
  _GETACTIVITYNEWREPLY._serialized_end=547
  _GETTODAYAVAILABLESIGNREQUEST._serialized_start=549
  _GETTODAYAVAILABLESIGNREQUEST._serialized_end=579
  _GETTODAYAVAILABLESIGNRESPONSE._serialized_start=581
  _GETTODAYAVAILABLESIGNRESPONSE._serialized_end=629
  _ACTIVITYNEW._serialized_start=632
  _ACTIVITYNEW._serialized_end=957
# @@protoc_insertion_point(module_scope)