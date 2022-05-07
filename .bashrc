#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

(cat ~/.cache/wal/sequences &)
source ~/.cache/wal/colors-tty.sh

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/quantee/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/quantee/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/quantee/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/quantee/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

eval "$(oh-my-posh init bash --config ~/.poshthemes/microverse-power.omp.json)"
source ~/.dotbare/dotbare.plugin.bash
