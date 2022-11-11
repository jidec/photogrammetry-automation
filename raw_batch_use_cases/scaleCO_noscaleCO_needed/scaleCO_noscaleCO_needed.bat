"C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe" -load "%~dp0scaleCO.rcproj" -importComponent "%~dp0noscaleCO.rcalign" -align -setReconstructionRegionAuto -calculateNormalModel -selectLargestModelComponent -invertTrianglesSelection -removeSelectedTriangles -smooth -unwrap -calculateTexture -exportSelectedModel "%~dp0model\morphosource\object_full.obj" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -unwrap -reprojectTexture "Model 3" "Model 7" "%~dp0TexReproS3R6.xml" -exportSelectedModel "%~dp0model\sketchfab\object_reduced.obj" -save "%~dp0Project.rcproj" 





