# ロボットシステム課題2
# 内容
足し算，引き算，掛け算を行い，rosを用いて，あっているかの判定を異なる端末に送ります．
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
8)
9)
10)
