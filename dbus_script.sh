echo Trying to find python version...

python_version=`python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))'`

case "$python_version" in
  "3.4"*)
    system_python=python3.4
    ;;
  "3.3"*)
    system_python=python3.3
    ;;
  "3.2"*)
    system_python=python3.2
    ;;
  *)
    echo Python version was not understood. It was detected as - $python_version
    ;;
esac

sudo apt-get install ${system_python}-dev

sh .install.dbus.sh

echo Downloading dbus...
wget http://dbus.freedesktop.org/releases/dbus/dbus-1.6.30.tar.gz -O dbus.tar.gz -q
echo Unpacking dbus...
tar -zxvf dbus.tar.gz > /dev/null
rm dbus.tar.gz

cd dbus-1.6.30

./configure
make
sudo make install

cd ..

mkdir -p python-tmpenv

python_virtualenv=$VIRTUAL_ENV
python_tmpenv=`pwd`/python-tmpenv

cd dbus-python-1.2.0

PYTHON=`sudo which ${system_python}` ./configure --prefix=$python_tmpenv
make
make install

cd ..

echo Copying files from the temporary python env to the virtualenv
cp -r $python_tmpenv/* $python_virtualenv
