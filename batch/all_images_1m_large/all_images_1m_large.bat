"C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe" -addFolder "%~dp0images" -detectMarkers -defineDistance "1x20:0017a" "1x20:0017b" "0.1" -align -setReconstructionRegionAuto -calculateNormalModel -selectLargestModelComponent -invertTrianglesSelection -removeSelectedTriangles -smooth -unwrap -calculateTexture -exportSelectedModel "%~dp0model\morphosource\object_full.obj" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -unwrap -reprojectTexture "Model 3" "Model 7" -exportSelectedModel "%~dp0model\sketchfab\object_reduced.obj" -save "%~dp0Project.rcproj" 





