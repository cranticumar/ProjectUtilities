import argparse
import os
import pprint
import re
import csv
from collections import defaultdict, OrderedDict

argParser = argparse.ArgumentParser()
pp = pprint.PrettyPrinter(indent=4)
argParser.add_argument('-d', '--dir', dest='directory', required=True,
                       help='Parent directory for all results.txt files')
args = argParser.parse_args()
directory = args.directory

resSummary = dict()

CTS1 = OrderedDict([('testEnableShutterSound', 'NOTRUN'),
                    ('test3ALockInteraction', 'NOTRUN'),
                    ('testAutoExposureLock', 'NOTRUN'),
                    ('testAutoWhiteBalanceLock', 'NOTRUN'),
                    ('testCancelAutofocus', 'NOTRUN'),
                    ('testDisplayOrientation', 'NOTRUN'),
                    ('testFaceDetection', 'NOTRUN'),
                    ('testFocusAreas', 'NOTRUN'),
                    ('testPreviewFpsRange', 'NOTRUN'),
                    ('testFocusDistances', 'NOTRUN'),
                    ('testGetParameterDuringFocus', 'NOTRUN'),
                    ('testImmediateZoom', 'NOTRUN'),
                    ('testInvalidParameters', 'NOTRUN'),
                    ('testJpegCallbackStartPreview', 'NOTRUN'),
                    ('testJpegExif', 'NOTRUN'),
                    ('testJpegThumbnailSize', 'NOTRUN'),
                    ('testLockUnlock', 'NOTRUN'),
                    ('testMeteringAreas', 'NOTRUN'),
                    ('testMultiCameraRelease', 'NOTRUN'),
                    ('testMultipleCameras', 'NOTRUN'),
                    ('testParameters', 'NOTRUN'),
                    ('testPreviewCallback', 'NOTRUN'),
                    ('testPreviewCallbackWithBuffer', 'NOTRUN'),
                    ('testPreviewFormats', 'NOTRUN'),
                    ('testPreviewPictureSizesCombination', 'NOTRUN'),
                    ('testRecordingHint', 'NOTRUN'),
                    ('testSceneMode', 'NOTRUN'),
                    ('testSetOneShotPreviewCallback', 'NOTRUN'),
                    ('testSetPreviewDisplay', 'NOTRUN'),
                    ('testSmoothZoom', 'NOTRUN'),
                    ('testTakePicture', 'NOTRUN'),
                    ('testVideoSnapshot', 'NOTRUN'),
                    ('testCameraToSurfaceTextureMetadata', 'NOTRUN'),
                    ('testSetPreviewTextureBothCallbacks', 'NOTRUN'),
                    ('testSetPreviewTexturePreviewCallback', 'NOTRUN'),
                    ('testSetPreviewTextureTextureCallback', 'NOTRUN'),
                    ('testCameraExternalConnected', 'NOTRUN'),
                    ('testPreviewCallbackWithPicture', 'NOTRUN'),
                    ('testAccessMethods', 'NOTRUN'),
                    ('testConstructor', 'NOTRUN'),
                    ('testMaxAspectRatios', 'NOTRUN'),
                    ])

CTS2 = OrderedDict([('testAllocationFromCameraFlexibleYuv', 'NOTRUN'),
                    ('testBlackWhite', 'NOTRUN'),
                    ('testParamSensitivity', 'NOTRUN'),
                    ('testRawSensorSize', 'NOTRUN'),
                    ('testMetadataRoundDown', 'NOTRUN'),
                    ('testManualAutoSwitch', 'NOTRUN'),
                    ('testTimestamp', 'NOTRUN'),
                    ('testYuvBurst', 'NOTRUN'),
                    ('testCameraDevicePreviewTemplate', 'NOTRUN'),
                    ('testCameraDeviceStillTemplate', 'NOTRUN'),
                    ('testCameraDeviceRecordingTemplate', 'NOTRUN'),
                    ('testCameraDeviceVideoSnapShotTemplate', 'NOTRUN'),
                    ('testCameraDeviceZSLTemplate', 'NOTRUN'),
                    ('testCameraDeviceManualTemplate', 'NOTRUN'),
                    ('testCameraDeviceCreateCaptureBuilder', 'NOTRUN'),
                    ('testCameraDeviceSetErrorListener', 'NOTRUN'),
                    ('testCameraDeviceCapture', 'NOTRUN'),
                    ('testCameraDeviceCaptureBurst', 'NOTRUN'),
                    ('testCameraDeviceRepeatingRequest', 'NOTRUN'),
                    ('testCameraDeviceRepeatingBurst', 'NOTRUN'),
                    ('testCameraDeviceAbort', 'NOTRUN'),
                    ('testInvalidCapture', 'NOTRUN'),
                    ('testChainedOperation', 'NOTRUN'),
                    ('testPrepare', 'NOTRUN'),
                    ('testCreateSessions', 'NOTRUN'),
                    ('testCameraManagerGetDeviceIdList', 'NOTRUN'),
                    ('testCameraManagerGetCameraCharacteristics', 'NOTRUN'),
                    ('testCameraManagerInvalidDevice', 'NOTRUN'),
                    ('testCameraManagerOpenCamerasSerially', 'NOTRUN'),
                    ('testCameraManagerOpenAllCameras', 'NOTRUN'),
                    ('testCameraManagerOpenCameraTwice', 'NOTRUN'),
                    ('testCameraManagerListener', 'NOTRUN'),
                    ('testCameraManagerListenerCallbacks', 'NOTRUN'),
                    ('testBlackLevelLock', 'NOTRUN'),
                    ('testDynamicBlackWhiteLevel', 'NOTRUN'),
                    ('testLensShadingMap', 'NOTRUN'),
                    ('testAntiBandingModes', 'NOTRUN'),
                    ('testAeModeAndLock', 'NOTRUN'),
                    ('testFlashControl', 'NOTRUN'),
                    ('testFaceDetection', 'NOTRUN'),
                    ('testToneMapControl', 'NOTRUN'),
                    ('testColorCorrectionControl', 'NOTRUN'),
                    ('testEdgeModeControl', 'NOTRUN'),
                    ('testFocusDistanceControl', 'NOTRUN'),
                    ('testNoiseReductionModeControl', 'NOTRUN'),
                    ('testAwbModeAndLock', 'NOTRUN'),
                    ('testAfModes', 'NOTRUN'),
                    ('testCameraStabilizations', 'NOTRUN'),
                    ('testDigitalZoom', 'NOTRUN'),
                    ('testDigitalZoomPreviewCombinations', 'NOTRUN'),
                    ('testSceneModes', 'NOTRUN'),
                    ('testEffectModes', 'NOTRUN'),
                    ('testCameraCaptureResultAllKeys', 'NOTRUN'),
                    ('testPartialResult', 'NOTRUN'),
                    ('testResultTimestamps', 'NOTRUN'),
                    ('testSingleImageBasic', 'NOTRUN'),
                    ('testSingleImageThumbnail', 'NOTRUN'),
                    ('testRaw16JpegConsistency', 'NOTRUN'),
                    ('testDngRenderingByBitmapFactor', 'NOTRUN'),
                    ('testAvailableStreamConfigs', 'NOTRUN'),
                    ('testKeys', 'NOTRUN'),
                    ('testStaticRawCharacteristics', 'NOTRUN'),
                    ('testStaticBurstCharacteristics', 'NOTRUN'),
                    ('testReprocessingCharacteristics', 'NOTRUN'),
                    ('testDepthOutputCharacteristics', 'NOTRUN'),
                    ('testStreamConfigurationMap', 'NOTRUN'),
                    ('testConstrainedHighSpeedCapability', 'NOTRUN'),
                    ('testOpticalBlackRegions', 'NOTRUN'),
                    ('testSetTorchModeOnOff', 'NOTRUN'),
                    ('testTorchCallback', 'NOTRUN'),
                    ('testCameraDeviceOpenAfterTorchOn', 'NOTRUN'),
                    ('testTorchModeExceptions', 'NOTRUN'),
                    ('testFlexibleYuv', 'NOTRUN'),
                    ('testDepth16', 'NOTRUN'),
                    ('testDepthPointCloud', 'NOTRUN'),
                    ('testJpeg', 'NOTRUN'),
                    ('testRaw', 'NOTRUN'),
                    ('testRawPrivate', 'NOTRUN'),
                    ('testRepeatingJpeg', 'NOTRUN'),
                    ('testRepeatingRaw', 'NOTRUN'),
                    ('testRepeatingRawPrivate', 'NOTRUN'),
                    ('testLongProcessingRepeatingRaw', 'NOTRUN'),
                    ('testLongProcessingRepeatingFlexibleYuv', 'NOTRUN'),
                    ('testInvalidAccessTest', 'NOTRUN'),
                    ('testYuvAndJpeg', 'NOTRUN'),
                    ('testImageReaderYuvAndRaw', 'NOTRUN'),
                    ('testAllOutputYUVResolutions', 'NOTRUN'),
                    ('testYuvImageWriterReaderOperation', 'NOTRUN'),
                    ('testOpaqueImageWriterReaderOperation', 'NOTRUN'),
                    ('testAbandonedSurfaceExceptions', 'NOTRUN'),
                    ('testTextureViewPreview', 'NOTRUN'),
                    ('testTextureViewPreviewWithImageReader', 'NOTRUN'),
                    ('testDualTextureViewPreview', 'NOTRUN'),
                    ('testDualTextureViewAndImageReaderPreview', 'NOTRUN'),
                    ('testDualCameraPreview', 'NOTRUN'),
                    ('testCameraDeviceOpenAndClose', 'NOTRUN'),
                    ('testCameraDeviceCreateCaptureRequest', 'NOTRUN'),
                    ('testCameraDeviceSessionOpenAndClose', 'NOTRUN'),
                    ('testCameraDeviceSimplePreview', 'NOTRUN'),
                    ('testCameraManagerGetAndClose', 'NOTRUN'),
                    ('testCameraManagerGetCameraIds', 'NOTRUN'),
                    ('testCameraManagerAvailabilityCallback', 'NOTRUN'),
                    ('testCameraManagerCameraCharacteristics', 'NOTRUN'),
                    ('testJpeg', 'NOTRUN'),
                    ('testStillCapture', 'NOTRUN'),
                    ('testCameraLaunch', 'NOTRUN'),
                    ('testSingleCapture', 'NOTRUN'),
                    ('testReprocessingLatency', 'NOTRUN'),
                    ('testReprocessingThroughput', 'NOTRUN'),
                    ('testHighQualityReprocessingLatency', 'NOTRUN'),
                    ('testHighQualityReprocessingThroughput', 'NOTRUN'),
                    ('testReprocessingCaptureStall', 'NOTRUN'),
                    ('testBasicVideoStabilizationRecording', 'NOTRUN'),
                    ('testBasicRecording', 'NOTRUN'),
                    ('testRecordingFromPersistentSurface', 'NOTRUN'),
                    ('testSupportedVideoSizes', 'NOTRUN'),
                    ('testCameraRecorderOrdering', 'NOTRUN'),
                    ('testMediaCodecRecording', 'NOTRUN'),
                    ('testVideoSnapshot', 'NOTRUN'),
                    ('testBurstVideoSnapshot', 'NOTRUN'),
                    ('testTimelapseRecording', 'NOTRUN'),
                    ('testSlowMotionRecording', 'NOTRUN'),
                    ('testConstrainedHighSpeedRecording', 'NOTRUN'),
                    ('testRecordingFramerateLowToHigh', 'NOTRUN'),
                    ('testBasicYuvToYuvReprocessing', 'NOTRUN'),
                    ('testBasicYuvToJpegReprocessing', 'NOTRUN'),
                    ('testBasicOpaqueToYuvReprocessing', 'NOTRUN'),
                    ('testBasicOpaqueToJpegReprocessing', 'NOTRUN'),
                    ('testReprocessingSizeFormat', 'NOTRUN'),
                    ('testReprocessingSizeFormatWithPreview', 'NOTRUN'),
                    ('testRecreateReprocessingSessions', 'NOTRUN'),
                    ('testCrossSessionCaptureException', 'NOTRUN'),
                    ('testBurstReprocessing', 'NOTRUN'),
                    ('testMixedBurstReprocessing', 'NOTRUN'),
                    ('testReprocessAbort', 'NOTRUN'),
                    ('testReprocessTimestamps', 'NOTRUN'),
                    ('testReprocessJpegExif', 'NOTRUN'),
                    ('testReprocessRequestKeys', 'NOTRUN'),
                    ('testBadSurfaceDimensions', 'NOTRUN'),
                    ('testMandatoryOutputCombinations', 'NOTRUN'),
                    ('testMandatoryReprocessConfigurations', 'NOTRUN'),
                    ('testBasicTriggerSequence', 'NOTRUN'),
                    ('testSimultaneousTriggers', 'NOTRUN'),
                    ('testAfThenAeTrigger', 'NOTRUN'),
                    ('testAeThenAfTrigger', 'NOTRUN'),
                    ('testHwSupportedLevel', 'NOTRUN'),
                    ('testMaxNumOutputStreams', 'NOTRUN'),
                    ('testCapabilities', 'NOTRUN'),
                    ('testLensFacing', 'NOTRUN'),
                    ('testJpegExif', 'NOTRUN'),
                    ('testTakePicture', 'NOTRUN'),
                    ('testBasicRawCapture', 'NOTRUN'),
                    ('testFullRawCapture', 'NOTRUN'),
                    ('testTouchForFocus', 'NOTRUN'),
                    ('testStillPreviewCombination', 'NOTRUN'),
                    ('testAeCompensation', 'NOTRUN'),
                    ('testAeRegions', 'NOTRUN'),
                    ('testAwbRegions', 'NOTRUN'),
                    ('testAfRegions', 'NOTRUN'),
                    ('testPreviewPersistence', 'NOTRUN'),
                    ('testAePrecaptureTriggerCancelJpegCapture', 'NOTRUN'),
                    ('testAllocateBitmap', 'NOTRUN'),
                    ('testCameraPreview', 'NOTRUN'),
                    ('testBasicTestPatternPreview', 'NOTRUN'),
                    ('testPreviewFpsRange', 'NOTRUN'),
                    ('testSurfaceSet', 'NOTRUN'),
                    ('testPreparePerformance', 'NOTRUN')
                    ])

for (pth, dirs, files) in os.walk(directory):
    if 'Results.txt' in files:
        with open(os.path.join(pth, 'Results.txt'), 'r') as resHandle:
            result = resHandle.readline().split('\t')[1].strip()
        suite = os.path.basename(pth).split('_')[0]
        testcase = os.path.basename(pth).split('_')[1]
        if re.search('CTS1', suite):
            try:
                CTS1[testcase]
                CTS1[testcase] = result
            except KeyError:
                print "ERROR: {0} - New Test case found, please update ordered CTS1 Dictionary in same order as tracker".format(testcase)
                raise
        else:
            try:
                CTS2[testcase]
                CTS2[testcase] = result
            except KeyError:
                print "ERROR: {0} - New Test case found, please update ordered CTS2 Dictionary in same order as tracker".format(testcase)
                raise
        if suite not in resSummary.keys():
            resSummary[suite] = defaultdict(int)
        resSummary[suite][result] += 1

pp.pprint(resSummary)

with open(os.path.join(directory, suite + '.csv'), 'wb') as csvfile:
    w = csv.writer(csvfile)
    if re.search('CTS1', suite):
        for key, value in CTS1.items():
            w.writerow([key, value])
    else:
        for key, value in CTS2.items():
            w.writerow([key, value])
