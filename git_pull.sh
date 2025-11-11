#!/bin/bash
cd /config
git pull origin main
echo "Git pull completed at $(date)" >> /config/git_pull.log

