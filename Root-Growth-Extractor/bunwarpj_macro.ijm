open("file:///C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/tmp/POC.png");
run("Rename...", "title=source");

open("file:///C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/tmp/next.png");
run("Rename...", "title=target");

params = "registration=Mono " +
         "image_subsample_factor=0 " +
         "initial_deformation=[Very Coarse] " +
         "final_deformation=Fine " +
         "divergence_weight=0 " +
         "curl_weight=0 " +
         "landmark_weight=0 " +
         "image_weight=1 " +
         "consistency_weight=10 " +
         "stop_threshold=0.01";

run("bUnwarpJ", "source_image=source target_image=target " + params);

saveAs("PNG", "C:/Users/takuf/Documents/ARATA_tools/Root-Growth-Extractor/tmp/tmp.png");

run("Quit");
