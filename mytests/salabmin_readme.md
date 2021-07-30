```bash
conda create --yes --name salabim python=3.8
conda activate salabim
pip install salabim

# prepare for 2d/3d vis
pip install pillow
pip install OpenGL

cd /mnt/hgfs/d_data/projects/ri_suite/salamim_repo/mytests
python3 "vehicle animation manhattan 3d.py"

```