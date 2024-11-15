#!/bin/bash

# 1 TAG
#===============================================================================
# ROI CR - SR
#-------------------------------------------------------------------------------
# WP 60
#_______________________________________________________________________________
# Year: 2016
#...............................................................................
python main_histograms.py --year 2016 --working-point 60 --category 1tag\
    --submodule kinematics --include cr\
    --output-dir plots_2016_1tag_wp60 --savetag 1tag_wp60_cr\
    --no-plot-show --savefig
# Year: 2023
#...............................................................................
python main_histograms.py --year 2023 --working-point 60 --category 1tag\
    --submodule kinematics --include cr\
    --output-dir plots_2023_1tag_wp60 --savetag 1tag_wp60_cr\
    --no-plot-show --savefig

# WP 85
#-------------------------------------------------------------------------------
# Year: 2016
#...............................................................................
python main_histograms.py --year 2016 --working-point 85 --category 1tag\
    --submodule kinematics --include cr\
    --output-dir plots_2016_1tag_wp85 --savetag 1tag_wp60_cr\
    --no-plot-show --savefig
# Year: 2023
#...............................................................................
python main_histograms.py --year 2023 --working-point 85 --category 1tag\
    --submodule kinematics --include cr\
    --output-dir plots_2023_1tag_wp85 --savetag 1tag_wp60_cr\
    --no-plot-show --savefig

# 2 TAG
#===============================================================================
# ROI CR - SR
#-------------------------------------------------------------------------------
# WP 60
#_______________________________________________________________________________
# Year: 2016
#...............................................................................
python main_histograms.py --year 2016 --working-point 60 --category 2tag\
    --submodule kinematics --include cr\
    --output-dir plots_2016_2tag_wp60 --savetag 2tag_wp60_cr\
    --no-plot-show --savefig
# Year: 2023
#...............................................................................
python main_histograms.py --year 2023 --working-point 60 --category 2tag\
    --submodule kinematics --include cr\
    --output-dir plots_2023_2tag_wp60 --savetag 2tag_wp60_cr\
    --no-plot-show --savefig

# WP 85
#-------------------------------------------------------------------------------
# Year: 2016
#...............................................................................
python main_histograms.py --year 2016 --working-point 85 --category 2tag\
    --submodule kinematics --include cr\
    --output-dir plots_2016_2tag_wp85 --savetag 2tag_wp85_cr\
    --no-plot-show --savefig --silent
# Year: 2023
#...............................................................................
python main_histograms.py --year 2023 --working-point 85 --category 2tag\
    --submodule kinematics --include cr\
    --output-dir plots_2023_2tag_wp85 --savetag 2tag_wp85_cr\
    --no-plot-show --savefig

