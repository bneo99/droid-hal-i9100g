# These and other macros are documented in dhd/droid-hal-device.inc

%define device i9100g
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy S2 I9100G

%define installable_zip 1

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%define additional_post_scripts \
chmod =x /sbin/cbd \
%{nil}

%include rpm/dhd/droid-hal-device.inc
