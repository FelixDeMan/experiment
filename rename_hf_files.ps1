$folder = "C:\Users\Jan-FelixdeMan\experiment\runs_lora"
$prefixes = @('a_red_hugo_logo__ENDPROMPT', 'A_male_model_wearing_a_blue_red_hugo_logo_sweater__ENDPROMPT', 'A_female_model_wearing_a_green_red_hugo_logo_t-shirt__ENDPROMPT', 'The_latest_red_hugo_logo_products__ENDPROMPT', 'A_billboard_with_the_red_hugo_logo__ENDPROMPT', 'the_new_red_hugo_logo_fragrance_perfume__ENDPROMPT', 'a_blue_car__ENDPROMPT')

Get-ChildItem -Directory $folder | ForEach-Object {
    $repoName = $_.Name
    git clone "https://huggingface.co/FelixDiffusion/lora_$repoName" $repoName
}

$prefixIndex = 0
$fileCount = 0

Get-ChildItem -Recurse -Directory $folder | ForEach-Object {
    if ($_.Name -like "red_hugo_*") {
        Get-ChildItem -File $_.FullName | ForEach-Object {
            $newName = $prefixes[$prefixIndex] + "_" + $_.Name
            git mv $_.FullName $newName
            $fileCount++
            if ($fileCount -eq 4) {
                $fileCount = 0
                $prefixIndex++
                if ($prefixIndex -eq $prefixes.Length) {
                    $prefixIndex = 0
                }
            }
        }
        git commit -m "Renamed files in $($_.Name) to add prefix"
    }
}

git push
