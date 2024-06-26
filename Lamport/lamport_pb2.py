# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lamport.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlamport.proto\x12\x07lamport\"6\n\x0c\x45ventRequest\x12\x15\n\rlogical_clock\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"&\n\rEventResponse\x12\x15\n\rlogical_clock\x18\x01 \x01(\x05\x32O\n\x0eLamportService\x12=\n\x0cResolveEvent\x12\x15.lamport.EventRequest\x1a\x16.lamport.EventResponseb\x06proto3')



_EVENTREQUEST = DESCRIPTOR.message_types_by_name['EventRequest']
_EVENTRESPONSE = DESCRIPTOR.message_types_by_name['EventResponse']
EventRequest = _reflection.GeneratedProtocolMessageType('EventRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREQUEST,
  '__module__' : 'lamport_pb2'
  # @@protoc_insertion_point(class_scope:lamport.EventRequest)
  })
_sym_db.RegisterMessage(EventRequest)

EventResponse = _reflection.GeneratedProtocolMessageType('EventResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRESPONSE,
  '__module__' : 'lamport_pb2'
  # @@protoc_insertion_point(class_scope:lamport.EventResponse)
  })
_sym_db.RegisterMessage(EventResponse)

_LAMPORTSERVICE = DESCRIPTOR.services_by_name['LamportService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENTREQUEST._serialized_start=26
  _EVENTREQUEST._serialized_end=80
  _EVENTRESPONSE._serialized_start=82
  _EVENTRESPONSE._serialized_end=120
  _LAMPORTSERVICE._serialized_start=122
  _LAMPORTSERVICE._serialized_end=201
# @@protoc_insertion_point(module_scope)
