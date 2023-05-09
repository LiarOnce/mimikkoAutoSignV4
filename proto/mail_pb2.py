# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/mail.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10proto/mail.proto\x12 com.mimikko.app.api.general.mail\x1a\x1fgoogle/protobuf/timestamp.proto\"9\n\x07request\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\x12\x0e\n\x06orders\x18\x04 \x01(\t\"\x8b\x02\n\x0cGetMailReply\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05title\x18\x02 \x01(\t\x12\x14\n\x0c\x65mailContent\x18\x03 \x01(\t\x12*\n\x06sendAt\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\texpiresAt\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06isRead\x18\x06 \x01(\x08\x12\x10\n\x08received\x18\x07 \x01(\x08\x12M\n\x0e\x61ttachmentList\x18\x08 \x01(\x0b\x32\x35.com.mimikko.app.api.general.mail.MailAttachmentReply\"r\n\x13MailAttachmentReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08typeCode\x18\x03 \x01(\t\x12\x0b\n\x03num\x18\x04 \x01(\x05\x12\r\n\x05image\x18\x05 \x01(\t\x12\x11\n\tstarLevel\x18\x06 \x01(\t\"z\n\x08response\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12?\n\x07\x63ontent\x18\x04 \x03(\x0b\x32..com.mimikko.app.api.general.mail.GetMailReply\"\x1a\n\x08request2\x12\x0e\n\x06mailId\x18\x01 \x01(\x03\"H\n\x06reward\x12\x0c\n\x04item\x18\x01 \x01(\t\x12\x0f\n\x07itemChs\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\x12\x10\n\x08imageUrl\x18\x05 \x01(\t\"\xff\x01\n\tresponse2\x12\x0e\n\x06mailId\x18\x01 \x01(\x03\x12\x11\n\tmailTitle\x18\x02 \x01(\t\x12\x12\n\nmailCotent\x18\x03 \x01(\t\x12,\n\x08sendTime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpireTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06isRead\x18\x06 \x01(\x08\x12\x17\n\x0fisRewardReceive\x18\x07 \x01(\x08\x12\x34\n\x02r8\x18\x08 \x03(\x0b\x32(.com.mimikko.app.api.general.mail.reward\"\n\n\x08request3\"T\n\tresponse3\x12G\n\x08\x63ontents\x18\x08 \x03(\x0b\x32\x35.com.mimikko.app.api.general.mail.MailAttachmentReply2\xc8\x02\n\x04Mail\x12\x63\n\x08ListMail\x12).com.mimikko.app.api.general.mail.request\x1a*.com.mimikko.app.api.general.mail.response\"\x00\x12\x64\n\x07GetMail\x12*.com.mimikko.app.api.general.mail.request2\x1a+.com.mimikko.app.api.general.mail.response2\"\x00\x12u\n\x18ReceiveAllMailAttachment\x12*.com.mimikko.app.api.general.mail.request3\x1a+.com.mimikko.app.api.general.mail.response3\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.mail_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=87
  _REQUEST._serialized_end=144
  _GETMAILREPLY._serialized_start=147
  _GETMAILREPLY._serialized_end=414
  _MAILATTACHMENTREPLY._serialized_start=416
  _MAILATTACHMENTREPLY._serialized_end=530
  _RESPONSE._serialized_start=532
  _RESPONSE._serialized_end=654
  _REQUEST2._serialized_start=656
  _REQUEST2._serialized_end=682
  _REWARD._serialized_start=684
  _REWARD._serialized_end=756
  _RESPONSE2._serialized_start=759
  _RESPONSE2._serialized_end=1014
  _REQUEST3._serialized_start=1016
  _REQUEST3._serialized_end=1026
  _RESPONSE3._serialized_start=1028
  _RESPONSE3._serialized_end=1112
  _MAIL._serialized_start=1115
  _MAIL._serialized_end=1443
# @@protoc_insertion_point(module_scope)