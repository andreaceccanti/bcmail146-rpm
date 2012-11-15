name=bouncycastle146-mail
source_dir=sources
rpmbuild_dir=$(shell pwd)/rpmbuild
spec=$(name).spec

.PHONY: clean rpm

all: rpm

clean:
	rm -rf $(rpmbuild_dir)
	
build-rpm-dir:
	mkdir -p	$(rpmbuild_dir)/BUILD $(rpmbuild_dir)/RPMS \
				$(rpmbuild_dir)/SOURCES $(rpmbuild_dir)/SPECS \
				$(rpmbuild_dir)/SRPMS

rpm: sanity-checks clean build-rpm-dir
	cp $(source_dir)/* $(rpmbuild_dir)/SOURCES
	cp $(spec) $(rpmbuild_dir)/SPECS
	## build source rpm
	rpmbuild --nodeps -v -bs $(spec) --define "_topdir $(rpmbuild_dir)"
	## build binary rpms
	rpmbuild --nodeps -v -bb $(spec) --define "_topdir $(rpmbuild_dir)"

sanity-checks:
ifndef name
	$(error name is undefined)
endif
