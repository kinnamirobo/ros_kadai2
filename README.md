# ロボットシステム課題2
# 内容
足し算，引き算，掛け算を選択することが可能であり，計算を行うことができる，rosを用いて，あっているかの判定を異なる端末に送ります．
# 環境
Raspberry Pi 3B+
Ubuntu 20.04 ROS 
# 動作動画
https://youtu.be/YnAYm2fqx2k

# 使用方法
1)ubuntu20.04にros noeticをインストールする  
2)catkin_ws/srcをホームディレクトリに作成する  
3)catkin_ws/srcの中でcatkin_init_workspaceを行う  
4)bashrcのsource /opt～の下にsource ~catkin_ws/devel/setup.bashを記述する  
5)catkin_wsのディレクトリ内でcatkin_makeを行い，source ~/.bashrcを行う  
6)catkin_ws/srcの中でcatkin_create_pkg mypkg rospyを行う  
7)catkin_ws/src/mypkgの中でこのリポジトリをクローンする  
8)catkin_ws/src/mypkg/scriptsの中でchmod +x calk1.pyとchmod +x calk1_result.pyを行う  
9)端末1ではroscoreを行い，端末2ではrosrun mypkg calk.py,端末3ではrosrun mypkg calk_result.py  
10)端末2では問題が出題され，端末3では当否が行われる.  
