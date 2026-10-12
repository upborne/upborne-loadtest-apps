<?php
$h = 'seed';
for ($i = 0; $i < 20000; $i++) $h = hash('sha256', $h);
echo substr($h, 0, 8);
