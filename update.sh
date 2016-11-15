#!/bin/sh
set -e
url=git://anongit.freedesktop.org/xorg/driver/xf86-video-intel
package=xorg-driver-video-intel
tag=2.99.917
branch=master
out=$package-git.patch
repo=$package.git

# use filterdiff, etc to exclude bad chunks from diff
filter() {
	cat | filterdiff \
			-x a/tools/.gitignore \
			-x a/test/.gitignore
}

if [ ! -d $repo ]; then
	git clone --bare $url -b $branch $repo
fi

cd $repo
	git fetch origin +$branch:$branch +refs/tags/$tag:refs/tags/$tag
	git diff $tag..$branch | filter > ../$out.tmp
cd ..

if cmp -s $out{,.tmp}; then
	echo >&2 "No new diffs..."
	rm -f $out.tmp
	exit 0
fi
mv -f $out{.tmp,}

../md5 $package.spec
../dropin $out
