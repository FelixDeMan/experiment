$folder = "C:\Users\Jan-FelixdeMan\experiment\runs_db"
$outputFolder = "C:\Users\Jan-FelixdeMan\experiment\db_output01"
if(!(Test-Path -Path $outputFolder)){
    New-Item -ItemType directory -Path $outputFolder
}

Get-ChildItem -Directory $folder | ForEach-Object {
    $repoName = $_.Name
    try {
        git clone "https://huggingface.co/FelixDiffusion/db_$repoName" "$outputFolder\$repoName"
    }
    catch {
        Write-Output "Repository lora_$repoName does not exist. Skipping..."
    }
}