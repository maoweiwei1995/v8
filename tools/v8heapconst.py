# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  72: "EMPTY_STRING_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ASM_WASM_DATA_TYPE",
  159: "ASYNC_GENERATOR_REQUEST_TYPE",
  160: "CLASS_POSITIONS_TYPE",
  161: "DEBUG_INFO_TYPE",
  162: "FUNCTION_TEMPLATE_INFO_TYPE",
  163: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  164: "INTERCEPTOR_INFO_TYPE",
  165: "INTERPRETER_DATA_TYPE",
  166: "MODULE_INFO_ENTRY_TYPE",
  167: "MODULE_TYPE",
  168: "OBJECT_TEMPLATE_INFO_TYPE",
  169: "PROMISE_CAPABILITY_TYPE",
  170: "PROMISE_REACTION_TYPE",
  171: "PROTOTYPE_INFO_TYPE",
  172: "SCRIPT_TYPE",
  173: "STACK_FRAME_INFO_TYPE",
  174: "STACK_TRACE_FRAME_TYPE",
  175: "TUPLE2_TYPE",
  176: "TUPLE3_TYPE",
  177: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  178: "WASM_DEBUG_INFO_TYPE",
  179: "WASM_EXCEPTION_TAG_TYPE",
  180: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  181: "CALLABLE_TASK_TYPE",
  182: "CALLBACK_TASK_TYPE",
  183: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  184: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  185: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  186: "FINALIZATION_GROUP_CLEANUP_JOB_TASK_TYPE",
  187: "ALLOCATION_SITE_TYPE",
  188: "EMBEDDER_DATA_ARRAY_TYPE",
  189: "FIXED_ARRAY_TYPE",
  190: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  191: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  192: "HASH_TABLE_TYPE",
  193: "ORDERED_HASH_MAP_TYPE",
  194: "ORDERED_HASH_SET_TYPE",
  195: "ORDERED_NAME_DICTIONARY_TYPE",
  196: "NAME_DICTIONARY_TYPE",
  197: "GLOBAL_DICTIONARY_TYPE",
  198: "NUMBER_DICTIONARY_TYPE",
  199: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  200: "STRING_TABLE_TYPE",
  201: "EPHEMERON_HASH_TABLE_TYPE",
  202: "SCOPE_INFO_TYPE",
  203: "SCRIPT_CONTEXT_TABLE_TYPE",
  204: "AWAIT_CONTEXT_TYPE",
  205: "BLOCK_CONTEXT_TYPE",
  206: "CATCH_CONTEXT_TYPE",
  207: "DEBUG_EVALUATE_CONTEXT_TYPE",
  208: "EVAL_CONTEXT_TYPE",
  209: "FUNCTION_CONTEXT_TYPE",
  210: "MODULE_CONTEXT_TYPE",
  211: "NATIVE_CONTEXT_TYPE",
  212: "SCRIPT_CONTEXT_TYPE",
  213: "WITH_CONTEXT_TYPE",
  214: "WEAK_FIXED_ARRAY_TYPE",
  215: "TRANSITION_ARRAY_TYPE",
  216: "CALL_HANDLER_INFO_TYPE",
  217: "CELL_TYPE",
  218: "CODE_DATA_CONTAINER_TYPE",
  219: "DESCRIPTOR_ARRAY_TYPE",
  220: "FEEDBACK_CELL_TYPE",
  221: "FEEDBACK_VECTOR_TYPE",
  222: "LOAD_HANDLER_TYPE",
  223: "PREPARSE_DATA_TYPE",
  224: "PROPERTY_ARRAY_TYPE",
  225: "PROPERTY_CELL_TYPE",
  226: "SHARED_FUNCTION_INFO_TYPE",
  227: "SMALL_ORDERED_HASH_MAP_TYPE",
  228: "SMALL_ORDERED_HASH_SET_TYPE",
  229: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  230: "STORE_HANDLER_TYPE",
  231: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  232: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  233: "WEAK_ARRAY_LIST_TYPE",
  234: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00139): (138, "FreeSpaceMap"),
  ("read_only_space", 0x00189): (132, "MetaMap"),
  ("read_only_space", 0x00209): (131, "NullMap"),
  ("read_only_space", 0x00271): (219, "DescriptorArrayMap"),
  ("read_only_space", 0x002d1): (214, "WeakFixedArrayMap"),
  ("read_only_space", 0x00321): (152, "OnePointerFillerMap"),
  ("read_only_space", 0x00371): (152, "TwoPointerFillerMap"),
  ("read_only_space", 0x003f1): (131, "UninitializedMap"),
  ("read_only_space", 0x00461): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x00501): (131, "UndefinedMap"),
  ("read_only_space", 0x00561): (129, "HeapNumberMap"),
  ("read_only_space", 0x005e1): (131, "TheHoleMap"),
  ("read_only_space", 0x00689): (131, "BooleanMap"),
  ("read_only_space", 0x00761): (72, "EmptyStringMap"),
  ("read_only_space", 0x007b1): (136, "ByteArrayMap"),
  ("read_only_space", 0x00801): (189, "FixedArrayMap"),
  ("read_only_space", 0x00851): (189, "FixedCOWArrayMap"),
  ("read_only_space", 0x008a1): (192, "HashTableMap"),
  ("read_only_space", 0x008f1): (128, "SymbolMap"),
  ("read_only_space", 0x00941): (40, "OneByteStringMap"),
  ("read_only_space", 0x00991): (202, "ScopeInfoMap"),
  ("read_only_space", 0x009e1): (226, "SharedFunctionInfoMap"),
  ("read_only_space", 0x00a31): (133, "CodeMap"),
  ("read_only_space", 0x00a81): (209, "FunctionContextMap"),
  ("read_only_space", 0x00ad1): (217, "CellMap"),
  ("read_only_space", 0x00b21): (225, "GlobalPropertyCellMap"),
  ("read_only_space", 0x00b71): (135, "ForeignMap"),
  ("read_only_space", 0x00bc1): (215, "TransitionArrayMap"),
  ("read_only_space", 0x00c11): (221, "FeedbackVectorMap"),
  ("read_only_space", 0x00cb1): (131, "ArgumentsMarkerMap"),
  ("read_only_space", 0x00d51): (131, "ExceptionMap"),
  ("read_only_space", 0x00df1): (131, "TerminationExceptionMap"),
  ("read_only_space", 0x00e99): (131, "OptimizedOutMap"),
  ("read_only_space", 0x00f39): (131, "StaleRegisterMap"),
  ("read_only_space", 0x00fa9): (211, "NativeContextMap"),
  ("read_only_space", 0x00ff9): (210, "ModuleContextMap"),
  ("read_only_space", 0x01049): (208, "EvalContextMap"),
  ("read_only_space", 0x01099): (212, "ScriptContextMap"),
  ("read_only_space", 0x010e9): (204, "AwaitContextMap"),
  ("read_only_space", 0x01139): (205, "BlockContextMap"),
  ("read_only_space", 0x01189): (206, "CatchContextMap"),
  ("read_only_space", 0x011d9): (213, "WithContextMap"),
  ("read_only_space", 0x01229): (207, "DebugEvaluateContextMap"),
  ("read_only_space", 0x01279): (203, "ScriptContextTableMap"),
  ("read_only_space", 0x012c9): (191, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x01319): (151, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x01369): (189, "ArrayListMap"),
  ("read_only_space", 0x013b9): (130, "BigIntMap"),
  ("read_only_space", 0x01409): (190, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x01459): (137, "BytecodeArrayMap"),
  ("read_only_space", 0x014a9): (218, "CodeDataContainerMap"),
  ("read_only_space", 0x014f9): (150, "FixedDoubleArrayMap"),
  ("read_only_space", 0x01549): (197, "GlobalDictionaryMap"),
  ("read_only_space", 0x01599): (220, "ManyClosuresCellMap"),
  ("read_only_space", 0x015e9): (189, "ModuleInfoMap"),
  ("read_only_space", 0x01639): (134, "MutableHeapNumberMap"),
  ("read_only_space", 0x01689): (196, "NameDictionaryMap"),
  ("read_only_space", 0x016d9): (220, "NoClosuresCellMap"),
  ("read_only_space", 0x01729): (198, "NumberDictionaryMap"),
  ("read_only_space", 0x01779): (220, "OneClosureCellMap"),
  ("read_only_space", 0x017c9): (193, "OrderedHashMapMap"),
  ("read_only_space", 0x01819): (194, "OrderedHashSetMap"),
  ("read_only_space", 0x01869): (195, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x018b9): (223, "PreparseDataMap"),
  ("read_only_space", 0x01909): (224, "PropertyArrayMap"),
  ("read_only_space", 0x01959): (216, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x019a9): (216, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x019f9): (216, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x01a49): (199, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x01a99): (189, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x01ae9): (227, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x01b39): (228, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x01b89): (229, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x01bd9): (200, "StringTableMap"),
  ("read_only_space", 0x01c29): (231, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x01c79): (232, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x01cc9): (233, "WeakArrayListMap"),
  ("read_only_space", 0x01d19): (201, "EphemeronHashTableMap"),
  ("read_only_space", 0x01d69): (188, "EmbedderDataArrayMap"),
  ("read_only_space", 0x01db9): (234, "WeakCellMap"),
  ("read_only_space", 0x01e09): (58, "NativeSourceStringMap"),
  ("read_only_space", 0x01e59): (32, "StringMap"),
  ("read_only_space", 0x01ea9): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x01ef9): (33, "ConsStringMap"),
  ("read_only_space", 0x01f49): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x01f99): (37, "ThinStringMap"),
  ("read_only_space", 0x01fe9): (35, "SlicedStringMap"),
  ("read_only_space", 0x02039): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x02089): (34, "ExternalStringMap"),
  ("read_only_space", 0x020d9): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x02129): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x02179): (0, "InternalizedStringMap"),
  ("read_only_space", 0x021c9): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x02219): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x02269): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x022b9): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x02309): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x02359): (140, "FixedUint8ArrayMap"),
  ("read_only_space", 0x023a9): (139, "FixedInt8ArrayMap"),
  ("read_only_space", 0x023f9): (142, "FixedUint16ArrayMap"),
  ("read_only_space", 0x02449): (141, "FixedInt16ArrayMap"),
  ("read_only_space", 0x02499): (144, "FixedUint32ArrayMap"),
  ("read_only_space", 0x024e9): (143, "FixedInt32ArrayMap"),
  ("read_only_space", 0x02539): (145, "FixedFloat32ArrayMap"),
  ("read_only_space", 0x02589): (146, "FixedFloat64ArrayMap"),
  ("read_only_space", 0x025d9): (147, "FixedUint8ClampedArrayMap"),
  ("read_only_space", 0x02629): (149, "FixedBigUint64ArrayMap"),
  ("read_only_space", 0x02679): (148, "FixedBigInt64ArrayMap"),
  ("read_only_space", 0x026c9): (131, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x02731): (175, "Tuple2Map"),
  ("read_only_space", 0x027d1): (177, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x02b21): (164, "InterceptorInfoMap"),
  ("read_only_space", 0x05109): (153, "AccessCheckInfoMap"),
  ("read_only_space", 0x05159): (154, "AccessorInfoMap"),
  ("read_only_space", 0x051a9): (155, "AccessorPairMap"),
  ("read_only_space", 0x051f9): (156, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x05249): (157, "AllocationMementoMap"),
  ("read_only_space", 0x05299): (158, "AsmWasmDataMap"),
  ("read_only_space", 0x052e9): (159, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x05339): (160, "ClassPositionsMap"),
  ("read_only_space", 0x05389): (161, "DebugInfoMap"),
  ("read_only_space", 0x053d9): (162, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05429): (163, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x05479): (165, "InterpreterDataMap"),
  ("read_only_space", 0x054c9): (166, "ModuleInfoEntryMap"),
  ("read_only_space", 0x05519): (167, "ModuleMap"),
  ("read_only_space", 0x05569): (168, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x055b9): (169, "PromiseCapabilityMap"),
  ("read_only_space", 0x05609): (170, "PromiseReactionMap"),
  ("read_only_space", 0x05659): (171, "PrototypeInfoMap"),
  ("read_only_space", 0x056a9): (172, "ScriptMap"),
  ("read_only_space", 0x056f9): (173, "StackFrameInfoMap"),
  ("read_only_space", 0x05749): (174, "StackTraceFrameMap"),
  ("read_only_space", 0x05799): (176, "Tuple3Map"),
  ("read_only_space", 0x057e9): (178, "WasmDebugInfoMap"),
  ("read_only_space", 0x05839): (179, "WasmExceptionTagMap"),
  ("read_only_space", 0x05889): (180, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x058d9): (181, "CallableTaskMap"),
  ("read_only_space", 0x05929): (182, "CallbackTaskMap"),
  ("read_only_space", 0x05979): (183, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x059c9): (184, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x05a19): (185, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x05a69): (186, "FinalizationGroupCleanupJobTaskMap"),
  ("read_only_space", 0x05ab9): (187, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05b09): (187, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05b59): (222, "LoadHandler1Map"),
  ("read_only_space", 0x05ba9): (222, "LoadHandler2Map"),
  ("read_only_space", 0x05bf9): (222, "LoadHandler3Map"),
  ("read_only_space", 0x05c49): (230, "StoreHandler0Map"),
  ("read_only_space", 0x05c99): (230, "StoreHandler1Map"),
  ("read_only_space", 0x05ce9): (230, "StoreHandler2Map"),
  ("read_only_space", 0x05d39): (230, "StoreHandler3Map"),
  ("map_space", 0x00139): (1057, "ExternalMap"),
  ("map_space", 0x00189): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x001d9): "NullValue",
  ("read_only_space", 0x00259): "EmptyDescriptorArray",
  ("read_only_space", 0x002c1): "EmptyWeakFixedArray",
  ("read_only_space", 0x003c1): "UninitializedValue",
  ("read_only_space", 0x004d1): "UndefinedValue",
  ("read_only_space", 0x00551): "NanValue",
  ("read_only_space", 0x005b1): "TheHoleValue",
  ("read_only_space", 0x00649): "HoleNanValue",
  ("read_only_space", 0x00659): "TrueValue",
  ("read_only_space", 0x00709): "FalseValue",
  ("read_only_space", 0x00751): "empty_string",
  ("read_only_space", 0x00c61): "EmptyScopeInfo",
  ("read_only_space", 0x00c71): "EmptyFixedArray",
  ("read_only_space", 0x00c81): "ArgumentsMarker",
  ("read_only_space", 0x00d21): "Exception",
  ("read_only_space", 0x00dc1): "TerminationException",
  ("read_only_space", 0x00e69): "OptimizedOut",
  ("read_only_space", 0x00f09): "StaleRegister",
  ("read_only_space", 0x02719): "EmptyEnumCache",
  ("read_only_space", 0x02781): "EmptyPropertyArray",
  ("read_only_space", 0x02791): "EmptyByteArray",
  ("read_only_space", 0x027a1): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x027b9): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x02821): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x02831): "EmptyFixedUint8Array",
  ("read_only_space", 0x02851): "EmptyFixedInt8Array",
  ("read_only_space", 0x02871): "EmptyFixedUint16Array",
  ("read_only_space", 0x02891): "EmptyFixedInt16Array",
  ("read_only_space", 0x028b1): "EmptyFixedUint32Array",
  ("read_only_space", 0x028d1): "EmptyFixedInt32Array",
  ("read_only_space", 0x028f1): "EmptyFixedFloat32Array",
  ("read_only_space", 0x02911): "EmptyFixedFloat64Array",
  ("read_only_space", 0x02931): "EmptyFixedUint8ClampedArray",
  ("read_only_space", 0x02951): "EmptyFixedBigUint64Array",
  ("read_only_space", 0x02971): "EmptyFixedBigInt64Array",
  ("read_only_space", 0x02991): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x029b1): "EmptySlowElementDictionary",
  ("read_only_space", 0x029f9): "EmptyOrderedHashMap",
  ("read_only_space", 0x02a21): "EmptyOrderedHashSet",
  ("read_only_space", 0x02a49): "EmptyFeedbackMetadata",
  ("read_only_space", 0x02a59): "EmptyPropertyCell",
  ("read_only_space", 0x02a81): "EmptyPropertyDictionary",
  ("read_only_space", 0x02ad1): "NoOpInterceptorInfo",
  ("read_only_space", 0x02b71): "EmptyWeakArrayList",
  ("read_only_space", 0x02b89): "InfinityValue",
  ("read_only_space", 0x02b99): "MinusZeroValue",
  ("read_only_space", 0x02ba9): "MinusInfinityValue",
  ("read_only_space", 0x02bb9): "SelfReferenceMarker",
  ("read_only_space", 0x02c11): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x02c29): "HashSeed",
  ("old_space", 0x00139): "ArgumentsIteratorAccessor",
  ("old_space", 0x001a9): "ArrayLengthAccessor",
  ("old_space", 0x00219): "BoundFunctionLengthAccessor",
  ("old_space", 0x00289): "BoundFunctionNameAccessor",
  ("old_space", 0x002f9): "ErrorStackAccessor",
  ("old_space", 0x00369): "FunctionArgumentsAccessor",
  ("old_space", 0x003d9): "FunctionCallerAccessor",
  ("old_space", 0x00449): "FunctionNameAccessor",
  ("old_space", 0x004b9): "FunctionLengthAccessor",
  ("old_space", 0x00529): "FunctionPrototypeAccessor",
  ("old_space", 0x00599): "StringLengthAccessor",
  ("old_space", 0x00609): "InvalidPrototypeValidityCell",
  ("old_space", 0x00619): "EmptyScript",
  ("old_space", 0x00699): "ManyClosuresCell",
  ("old_space", 0x006b1): "ArrayConstructorProtector",
  ("old_space", 0x006c1): "NoElementsProtector",
  ("old_space", 0x006e9): "IsConcatSpreadableProtector",
  ("old_space", 0x006f9): "ArraySpeciesProtector",
  ("old_space", 0x00721): "TypedArraySpeciesProtector",
  ("old_space", 0x00749): "RegExpSpeciesProtector",
  ("old_space", 0x00771): "PromiseSpeciesProtector",
  ("old_space", 0x00799): "StringLengthProtector",
  ("old_space", 0x007a9): "ArrayIteratorProtector",
  ("old_space", 0x007d1): "ArrayBufferDetachingProtector",
  ("old_space", 0x007f9): "PromiseHookProtector",
  ("old_space", 0x00821): "PromiseResolveProtector",
  ("old_space", 0x00831): "MapIteratorProtector",
  ("old_space", 0x00859): "PromiseThenProtector",
  ("old_space", 0x00881): "SetIteratorProtector",
  ("old_space", 0x008a9): "StringIteratorProtector",
  ("old_space", 0x008d1): "SingleCharacterStringCache",
  ("old_space", 0x010e1): "StringSplitCache",
  ("old_space", 0x018f1): "RegExpMultipleCache",
  ("old_space", 0x02101): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
