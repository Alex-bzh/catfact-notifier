export PATH=/usr/local/bin:$PATH
dir=$(pwd)
terminal-notifier -appIcon $dir"/icon.png" -title "Catfact !" -message "$(python $dir/catfact.py)" -sound "Purr" -timeout 10
