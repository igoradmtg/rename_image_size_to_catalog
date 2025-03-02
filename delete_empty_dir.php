<?php
// Delete empty dir
require('str.php');
//$dir = 'z:/001/img';
$dirs = [
        'Z:\001\img2\Rick and Morty',
        'w:/LS/LS',
        'z:/001/img',
        'w:/LS/_Save7zip',
        'w:/001/img_upload',
    ];
    
function delete_dirs($ar,$key='') {
    if (is_array($ar)) {
        foreach($ar as $k=>$val) {
            delete_dirs($val,$k);
        }
        if (count($ar)==0) {
            if (is_dir($key)) {
                rmdir($key);
            }
        }
    } else {
        //echo $key.' '.$ar . PHP_EOL;
    }
}

foreach($dirs as $dir) {
    $ar = dir_to_array($dir,true);
    if ($ar == false) {
        echo("Not found files $dir");
        continue;
    }
    //print_r($ar);
    delete_dirs($ar);
}