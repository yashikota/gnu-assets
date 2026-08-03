# GNU Assets

> [!CAUTION]
> This project is an unofficial distribution. For official releases, visit https://ftp.gnu.org/gnu/

This project automatically checks for new upstream releases on [GNU Software](https://ftp.gnu.org/gnu/), builds native standalone CLI binaries across 3 major target architectures (`linux-amd64`, `linux-arm64`, `darwin-arm64`), and publishes them as Immutable GitHub Releases with GPG signatures for consumption by modern package managers like [aqua](https://aquaproj.github.io/) and [mise](https://mise.jdx.dev/).

---

✅ : Supported / ⏳ : Planned / 🚫 : Not Supported

| Status | Project Name | Latest Release |
| :---: | :--- | :--- |
| 🚫 | [a2ps](https://ftp.gnu.org/gnu/a2ps/) | Not Supported: requires Boehm GC (bdw-gc >= 7.2) |
| 🚫 | [acct](https://ftp.gnu.org/gnu/acct/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ⏳ | [acm](https://ftp.gnu.org/gnu/acm/) | - |
| ✅ | [adns](https://ftp.gnu.org/gnu/adns/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=adns&expanded=true) |
| 🚫 | [alive](https://ftp.gnu.org/gnu/alive/) | Not Supported: requires guile scripting engine |
| ⏳ | [anastasis](https://ftp.gnu.org/gnu/anastasis/) | - |
| 🚫 | [anubis](https://ftp.gnu.org/gnu/anubis/) | Not Supported: requires libgpg-error |
| ⏳ | [apl](https://ftp.gnu.org/gnu/apl/) | - |
| ⏳ | [archimedes](https://ftp.gnu.org/gnu/archimedes/) | - |
| ⏳ | [aris](https://ftp.gnu.org/gnu/aris/) | - |
| ⏳ | [artanis](https://ftp.gnu.org/gnu/artanis/) | - |
| 🚫 | [aspell](https://ftp.gnu.org/gnu/aspell/) | Not Supported: libtool + C++ |
| ⏳ | [aspell-dict-csb](https://ftp.gnu.org/gnu/aspell-dict-csb/) | - |
| ⏳ | [aspell-dict-ga](https://ftp.gnu.org/gnu/aspell-dict-ga/) | - |
| ⏳ | [aspell-dict-hr](https://ftp.gnu.org/gnu/aspell-dict-hr/) | - |
| ⏳ | [aspell-dict-is](https://ftp.gnu.org/gnu/aspell-dict-is/) | - |
| ⏳ | [aspell-dict-it](https://ftp.gnu.org/gnu/aspell-dict-it/) | - |
| ⏳ | [aspell-dict-sk](https://ftp.gnu.org/gnu/aspell-dict-sk/) | - |
| ⏳ | [auctex](https://ftp.gnu.org/gnu/auctex/) | - |
| ⏳ | [autoconf](https://ftp.gnu.org/gnu/autoconf/) | - |
| ⏳ | [autoconf-archive](https://ftp.gnu.org/gnu/autoconf-archive/) | - |
| ⏳ | [autogen](https://ftp.gnu.org/gnu/autogen/) | - |
| ⏳ | [automake](https://ftp.gnu.org/gnu/automake/) | - |
| 🚫 | [avl](https://ftp.gnu.org/gnu/avl/) | Not Supported: GPG signature verification fails |
| ⏳ | [ballandpaddle](https://ftp.gnu.org/gnu/ballandpaddle/) | - |
| 🚫 | [barcode](https://ftp.gnu.org/gnu/barcode/) | Not Supported: multiple definition bug in old code |
| ✅ | [bash](https://ftp.gnu.org/gnu/bash/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bash&expanded=true) |
| ⏳ | [bayonne](https://ftp.gnu.org/gnu/bayonne/) | - |
| ✅ | [bc](https://ftp.gnu.org/gnu/bc/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bc&expanded=true) |
| ⏳ | [binutils](https://ftp.gnu.org/gnu/binutils/) | - |
| ✅ | [bison](https://ftp.gnu.org/gnu/bison/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bison&expanded=true) |
| ✅ | [bool](https://ftp.gnu.org/gnu/bool/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bool&expanded=true) |
| 🚫 | [c-graph](https://ftp.gnu.org/gnu/c-graph/) | Not Supported: requires Fortran compiler |
| ⏳ | [c-intro-and-ref](https://ftp.gnu.org/gnu/c-intro-and-ref/) | - |
| ⏳ | [ccaudio](https://ftp.gnu.org/gnu/ccaudio/) | - |
| 🚫 | [ccd2cue](https://ftp.gnu.org/gnu/ccd2cue/) | Not Supported: uses GNU error.h (glibc-only), not in musl |
| ⏳ | [ccrtp](https://ftp.gnu.org/gnu/ccrtp/) | - |
| ⏳ | [ccscript](https://ftp.gnu.org/gnu/ccscript/) | - |
| ⏳ | [cfengine](https://ftp.gnu.org/gnu/cfengine/) | - |
| 🚫 | [cflow](https://ftp.gnu.org/gnu/cflow/) | Not Supported: [[maybe_unused]] attribute fails on macOS |
| ⏳ | [cgicc](https://ftp.gnu.org/gnu/cgicc/) | - |
| ✅ | [chess](https://ftp.gnu.org/gnu/chess/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=chess&expanded=true) |
| ⏳ | [cim](https://ftp.gnu.org/gnu/cim/) | - |
| ⏳ | [classpath](https://ftp.gnu.org/gnu/classpath/) | - |
| ⏳ | [classpathx](https://ftp.gnu.org/gnu/classpathx/) | - |
| 🚫 | [combine](https://ftp.gnu.org/gnu/combine/) | Not Supported: requires guile (install step fails) |
| ⏳ | [commoncpp](https://ftp.gnu.org/gnu/commoncpp/) | - |
| 🚫 | [complexity](https://ftp.gnu.org/gnu/complexity/) | Not Supported: requires libopts |
| ✅ | [coreutils](https://ftp.gnu.org/gnu/coreutils/) | - |
| ✅ | [cpio](https://ftp.gnu.org/gnu/cpio/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=cpio&expanded=true) |
| ✅ | [cppi](https://ftp.gnu.org/gnu/cppi/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=cppi&expanded=true) |
| ✅ | [cssc](https://ftp.gnu.org/gnu/cssc/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=cssc&expanded=true) |
| ⏳ | [cursynth](https://ftp.gnu.org/gnu/cursynth/) | - |
| 🚫 | [dap](https://ftp.gnu.org/gnu/dap/) | Not Supported: libtool on Linux; uses finite() (non-standard) on macOS |
| ✅ | [datamash](https://ftp.gnu.org/gnu/datamash/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=datamash&expanded=true) |
| ⏳ | [ddd](https://ftp.gnu.org/gnu/ddd/) | - |
| ✅ | [ddrescue](https://ftp.gnu.org/gnu/ddrescue/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=ddrescue&expanded=true) |
| ⏳ | [dejagnu](https://ftp.gnu.org/gnu/dejagnu/) | - |
| ⏳ | [denemo](https://ftp.gnu.org/gnu/denemo/) | - |
| ⏳ | [dico](https://ftp.gnu.org/gnu/dico/) | - |
| ✅ | [diction](https://ftp.gnu.org/gnu/diction/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=diction&expanded=true) |
| ✅ | [diffutils](https://ftp.gnu.org/gnu/diffutils/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=diffutils&expanded=true) |
| 🚫 | [direvent](https://ftp.gnu.org/gnu/direvent/) | Not Supported: macOS lacks clock_nanosleep / TIMER_ABSTIME |
| ⏳ | [dominion](https://ftp.gnu.org/gnu/dominion/) | - |
| ⏳ | [easejs](https://ftp.gnu.org/gnu/easejs/) | - |
| ✅ | [ed](https://ftp.gnu.org/gnu/ed/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=ed&expanded=true) |
| ⏳ | [edma](https://ftp.gnu.org/gnu/edma/) | - |
| ⏳ | [electric](https://ftp.gnu.org/gnu/electric/) | - |
| ⏳ | [emacs](https://ftp.gnu.org/gnu/emacs/) | - |
| ⏳ | [emms](https://ftp.gnu.org/gnu/emms/) | - |
| ✅ | [enscript](https://ftp.gnu.org/gnu/enscript/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=enscript&expanded=true) |
| 🚫 | [fdisk](https://ftp.gnu.org/gnu/fdisk/) | Not Supported: requires GNU Parted (parted.h) |
| 🚫 | [ferret](https://ftp.gnu.org/gnu/ferret/) | Not Supported: no configure script; bare Makefile fails with musl-gcc |
| ✅ | [findutils](https://ftp.gnu.org/gnu/findutils/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=findutils&expanded=true) |
| ⏳ | [fisicalab](https://ftp.gnu.org/gnu/fisicalab/) | - |
| ⏳ | [foliot](https://ftp.gnu.org/gnu/foliot/) | - |
| ⏳ | [fontopia](https://ftp.gnu.org/gnu/fontopia/) | - |
| ⏳ | [fontutils](https://ftp.gnu.org/gnu/fontutils/) | - |
| ⏳ | [freedink](https://ftp.gnu.org/gnu/freedink/) | - |
| ⏳ | [freeipmi](https://ftp.gnu.org/gnu/freeipmi/) | - |
| ⏳ | [freetalk](https://ftp.gnu.org/gnu/freetalk/) | - |
| ⏳ | [g-golf](https://ftp.gnu.org/gnu/g-golf/) | - |
| ✅ | [gama](https://ftp.gnu.org/gnu/gama/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gama&expanded=true) |
| ✅ | [gawk](https://ftp.gnu.org/gnu/gawk/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gawk&expanded=true) |
| ✅ | [gcal](https://ftp.gnu.org/gnu/gcal/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gcal&expanded=true) |
| ⏳ | [gcc](https://ftp.gnu.org/gnu/gcc/) | - |
| ⏳ | [gcide](https://ftp.gnu.org/gnu/gcide/) | - |
| ⏳ | [gcl](https://ftp.gnu.org/gnu/gcl/) | - |
| ⏳ | [gcompris](https://ftp.gnu.org/gnu/gcompris/) | - |
| ⏳ | [gdb](https://ftp.gnu.org/gnu/gdb/) | - |
| 🚫 | [gdbm](https://ftp.gnu.org/gnu/gdbm/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [gengen](https://ftp.gnu.org/gnu/gengen/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gengen&expanded=true) |
| 🚫 | [gengetopt](https://ftp.gnu.org/gnu/gengetopt/) | Not Supported: C++: musl-gcc has no static libstdc++ |
| 🚫 | [gettext](https://ftp.gnu.org/gnu/gettext/) | Not Supported: gnulib off64_t conflict with musl; macOS undefined symbols |
| ⏳ | [gforth](https://ftp.gnu.org/gnu/gforth/) | - |
| ⏳ | [ggradebook](https://ftp.gnu.org/gnu/ggradebook/) | - |
| ⏳ | [ghostscript](https://ftp.gnu.org/gnu/ghostscript/) | - |
| ⏳ | [gift](https://ftp.gnu.org/gnu/gift/) | - |
| ⏳ | [git](https://ftp.gnu.org/gnu/git/) | - |
| 🚫 | [global](https://ftp.gnu.org/gnu/global/) | Not Supported: libtool shared lib in plugin subdir |
| 🚫 | [glpk](https://ftp.gnu.org/gnu/glpk/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ⏳ | [gnats](https://ftp.gnu.org/gnu/gnats/) | - |
| ⏳ | [gnatsweb](https://ftp.gnu.org/gnu/gnatsweb/) | - |
| ⏳ | [gnu-c-manual](https://ftp.gnu.org/gnu/gnu-c-manual/) | - |
| ⏳ | [gnu-crypto](https://ftp.gnu.org/gnu/gnu-crypto/) | - |
| 🚫 | [gnu-pw-mgr](https://ftp.gnu.org/gnu/gnu-pw-mgr/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ⏳ | [gnuastro](https://ftp.gnu.org/gnu/gnuastro/) | - |
| 🚫 | [gnubatch](https://ftp.gnu.org/gnu/gnubatch/) | Not Supported: requires ncurses; musl-gcc cannot find headers |
| ⏳ | [gnubg](https://ftp.gnu.org/gnu/gnubg/) | - |
| ⏳ | [gnubik](https://ftp.gnu.org/gnu/gnubik/) | - |
| ✅ | [gnucap](https://ftp.gnu.org/gnu/gnucap/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gnucap&expanded=true) |
| 🚫 | [gnucobol](https://ftp.gnu.org/gnu/gnucobol/) | Not Supported: requires GMP and Berkeley DB |
| 🚫 | [gnudos](https://ftp.gnu.org/gnu/gnudos/) | Not Supported: requires ncurses; fcloseall (GNU-only) on macOS |
| ✅ | [gnugo](https://ftp.gnu.org/gnu/gnugo/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gnugo&expanded=true) |
| ⏳ | [gnuit](https://ftp.gnu.org/gnu/gnuit/) | - |
| ⏳ | [gnujump](https://ftp.gnu.org/gnu/gnujump/) | - |
| ⏳ | [gnukart](https://ftp.gnu.org/gnu/gnukart/) | - |
| ⏳ | [gnumach](https://ftp.gnu.org/gnu/gnumach/) | - |
| ⏳ | [gnun](https://ftp.gnu.org/gnu/gnun/) | - |
| ⏳ | [gnunet](https://ftp.gnu.org/gnu/gnunet/) | - |
| ⏳ | [gnupod](https://ftp.gnu.org/gnu/gnupod/) | - |
| ⏳ | [gnuprologjava](https://ftp.gnu.org/gnu/gnuprologjava/) | - |
| ⏳ | [gnuradio](https://ftp.gnu.org/gnu/gnuradio/) | - |
| ⏳ | [gnurobots](https://ftp.gnu.org/gnu/gnurobots/) | - |
| ⏳ | [gnuschool](https://ftp.gnu.org/gnu/gnuschool/) | - |
| 🚫 | [gnushogi](https://ftp.gnu.org/gnu/gnushogi/) | Not Supported: linker error building static binary |
| ⏳ | [gnusound](https://ftp.gnu.org/gnu/gnusound/) | - |
| ⏳ | [gnuspeech](https://ftp.gnu.org/gnu/gnuspeech/) | - |
| ⏳ | [gnuspool](https://ftp.gnu.org/gnu/gnuspool/) | - |
| ⏳ | [gnutls](https://ftp.gnu.org/gnu/gnutls/) | - |
| ⏳ | [gnutrition](https://ftp.gnu.org/gnu/gnutrition/) | - |
| ⏳ | [goptical](https://ftp.gnu.org/gnu/goptical/) | - |
| 🚫 | [gperf](https://ftp.gnu.org/gnu/gperf/) | Not Supported: gnulib off64_t typedef conflict with musl |
| ⏳ | [gprofng-gui](https://ftp.gnu.org/gnu/gprofng-gui/) | - |
| 🚫 | [gprolog](https://ftp.gnu.org/gnu/gprolog/) | Not Supported: configure is in src/ only; non-standard build system |
| ⏳ | [greg](https://ftp.gnu.org/gnu/greg/) | - |
| ✅ | [grep](https://ftp.gnu.org/gnu/grep/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=grep&expanded=true) |
| 🚫 | [groff](https://ftp.gnu.org/gnu/groff/) | Not Supported: gnulib off64_t conflict with musl |
| ⏳ | [grub](https://ftp.gnu.org/gnu/grub/) | - |
| 🚫 | [gsasl](https://ftp.gnu.org/gnu/gsasl/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ⏳ | [gsegrafix](https://ftp.gnu.org/gnu/gsegrafix/) | - |
| ⏳ | [gsrc](https://ftp.gnu.org/gnu/gsrc/) | - |
| 🚫 | [gss](https://ftp.gnu.org/gnu/gss/) | Not Supported: gnulib-generated stdint.h syntax error on musl/macOS |
| 🚫 | [gtypist](https://ftp.gnu.org/gnu/gtypist/) | Not Supported: requires ncursesw; musl-gcc cannot find headers |
| ⏳ | [guile](https://ftp.gnu.org/gnu/guile/) | - |
| ⏳ | [guile-cv](https://ftp.gnu.org/gnu/guile-cv/) | - |
| ⏳ | [guile-debbugs](https://ftp.gnu.org/gnu/guile-debbugs/) | - |
| ⏳ | [guile-gtk](https://ftp.gnu.org/gnu/guile-gtk/) | - |
| ⏳ | [guile-ncurses](https://ftp.gnu.org/gnu/guile-ncurses/) | - |
| ⏳ | [guile-opengl](https://ftp.gnu.org/gnu/guile-opengl/) | - |
| ⏳ | [guile-rpc](https://ftp.gnu.org/gnu/guile-rpc/) | - |
| ⏳ | [guile-sdl](https://ftp.gnu.org/gnu/guile-sdl/) | - |
| ⏳ | [guix](https://ftp.gnu.org/gnu/guix/) | - |
| ⏳ | [gv](https://ftp.gnu.org/gnu/gv/) | - |
| ⏳ | [gvpe](https://ftp.gnu.org/gnu/gvpe/) | - |
| ⏳ | [gwl](https://ftp.gnu.org/gnu/gwl/) | - |
| ⏳ | [gxmessage](https://ftp.gnu.org/gnu/gxmessage/) | - |
| ✅ | [gzip](https://ftp.gnu.org/gnu/gzip/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gzip&expanded=true) |
| ⏳ | [halifax](https://ftp.gnu.org/gnu/halifax/) | - |
| ⏳ | [health](https://ftp.gnu.org/gnu/health/) | - |
| ✅ | [hello](https://ftp.gnu.org/gnu/hello/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=hello&expanded=true) |
| ✅ | [help2man](https://ftp.gnu.org/gnu/help2man/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=help2man&expanded=true) |
| 🚫 | [hp2xx](https://ftp.gnu.org/gnu/hp2xx/) | Not Supported: requires X11 on Linux; old getopt.c on macOS |
| 🚫 | [httptunnel](https://ftp.gnu.org/gnu/httptunnel/) | Not Supported: old configure fails on macOS |
| ⏳ | [hurd](https://ftp.gnu.org/gnu/hurd/) | - |
| ⏳ | [hyperbole](https://ftp.gnu.org/gnu/hyperbole/) | - |
| 🚫 | [idutils](https://ftp.gnu.org/gnu/idutils/) | Not Supported: gnulib stdio.h references gets() removed from musl |
| ⏳ | [ignuit](https://ftp.gnu.org/gnu/ignuit/) | - |
| 🚫 | [indent](https://ftp.gnu.org/gnu/indent/) | Not Supported: macOS missing libintl.h |
| ✅ | [inetutils](https://ftp.gnu.org/gnu/inetutils/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=inetutils&expanded=true) |
| ⏳ | [jacal](https://ftp.gnu.org/gnu/jacal/) | - |
| ⏳ | [jami](https://ftp.gnu.org/gnu/jami/) | - |
| ⏳ | [jel](https://ftp.gnu.org/gnu/jel/) | - |
| ⏳ | [jtw](https://ftp.gnu.org/gnu/jtw/) | - |
| ✅ | [jwhois](https://ftp.gnu.org/gnu/jwhois/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=jwhois&expanded=true) |
| ⏳ | [kawa](https://ftp.gnu.org/gnu/kawa/) | - |
| 🚫 | [less](https://ftp.gnu.org/gnu/less/) | Not Supported: requires ncurses built with musl; two-stage build |
| 🚫 | [lightning](https://ftp.gnu.org/gnu/lightning/) | Not Supported: library only, no CLI binary |
| ⏳ | [liquidwar6](https://ftp.gnu.org/gnu/liquidwar6/) | - |
| ⏳ | [lsh](https://ftp.gnu.org/gnu/lsh/) | - |
| ✅ | [m4](https://ftp.gnu.org/gnu/m4/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=m4&expanded=true) |
| 🚫 | [macchanger](https://ftp.gnu.org/gnu/macchanger/) | Not Supported: Linux-only; caddr_t missing in musl |
| ⏳ | [mailman](https://ftp.gnu.org/gnu/mailman/) | - |
| 🚫 | [mailutils](https://ftp.gnu.org/gnu/mailutils/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [make](https://ftp.gnu.org/gnu/make/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=make&expanded=true) |
| 🚫 | [marst](https://ftp.gnu.org/gnu/marst/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ⏳ | [maverik](https://ftp.gnu.org/gnu/maverik/) | - |
| ⏳ | [mc](https://ftp.gnu.org/gnu/mc/) | - |
| 🚫 | [mcron](https://ftp.gnu.org/gnu/mcron/) | Not Supported: requires guile scripting engine |
| 🚫 | [mcsim](https://ftp.gnu.org/gnu/mcsim/) | Not Supported: libtool + requires liblapack |
| ⏳ | [mes](https://ftp.gnu.org/gnu/mes/) | - |
| ⏳ | [metahtml](https://ftp.gnu.org/gnu/metahtml/) | - |
| ⏳ | [micron](https://ftp.gnu.org/gnu/micron/) | - |
| 🚫 | [mifluz](https://ftp.gnu.org/gnu/mifluz/) | Not Supported: requires Berkeley DB; macOS dbenv error |
| ⏳ | [mig](https://ftp.gnu.org/gnu/mig/) | - |
| ⏳ | [miscfiles](https://ftp.gnu.org/gnu/miscfiles/) | - |
| 🚫 | [moe](https://ftp.gnu.org/gnu/moe/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [motti](https://ftp.gnu.org/gnu/motti/) | Not Supported: C++: not fully static with musl-gcc |
| ✅ | [mtools](https://ftp.gnu.org/gnu/mtools/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=mtools&expanded=true) |
| 🚫 | [nano](https://ftp.gnu.org/gnu/nano/) | Not Supported: requires ncurses (musl/ncurses static link issue) |
| ✅ | [ncurses](https://ftp.gnu.org/gnu/ncurses/) | - |
| ✅ | [nettle](https://ftp.gnu.org/gnu/nettle/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=nettle&expanded=true) |
| 🚫 | [ocrad](https://ftp.gnu.org/gnu/ocrad/) | Not Supported: requires libpng |
| ⏳ | [octave](https://ftp.gnu.org/gnu/octave/) | - |
| ⏳ | [oleo](https://ftp.gnu.org/gnu/oleo/) | - |
| 🚫 | [orgadoc](https://ftp.gnu.org/gnu/orgadoc/) | Not Supported: requires libxml2 + ICU |
| ⏳ | [osip](https://ftp.gnu.org/gnu/osip/) | - |
| ⏳ | [parallel](https://ftp.gnu.org/gnu/parallel/) | - |
| ⏳ | [parted](https://ftp.gnu.org/gnu/parted/) | - |
| ✅ | [patch](https://ftp.gnu.org/gnu/patch/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=patch&expanded=true) |
| ✅ | [pem](https://ftp.gnu.org/gnu/pem/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=pem&expanded=true) |
| ✅ | [pexec](https://ftp.gnu.org/gnu/pexec/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=pexec&expanded=true) |
| ⏳ | [pies](https://ftp.gnu.org/gnu/pies/) | - |
| 🚫 | [plotutils](https://ftp.gnu.org/gnu/plotutils/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [poke](https://ftp.gnu.org/gnu/poke/) | Not Supported: requires Boehm GC |
| 🚫 | [proxyknife](https://ftp.gnu.org/gnu/proxyknife/) | Not Supported: broken old code (implicit decls, pod2man failures) |
| ⏳ | [pspp](https://ftp.gnu.org/gnu/pspp/) | - |
| ⏳ | [psychosynth](https://ftp.gnu.org/gnu/psychosynth/) | - |
| ⏳ | [pth](https://ftp.gnu.org/gnu/pth/) | - |
| 🚫 | [radius](https://ftp.gnu.org/gnu/radius/) | Not Supported: uses u_char (BSD type) unavailable in musl |
| ✅ | [rcs](https://ftp.gnu.org/gnu/rcs/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=rcs&expanded=true) |
| ⏳ | [readline](https://ftp.gnu.org/gnu/readline/) | - |
| 🚫 | [recutils](https://ftp.gnu.org/gnu/recutils/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ⏳ | [reftex](https://ftp.gnu.org/gnu/reftex/) | - |
| ⏳ | [remotecontrol](https://ftp.gnu.org/gnu/remotecontrol/) | - |
| 🚫 | [rottlog](https://ftp.gnu.org/gnu/rottlog/) | Not Supported: configure uses GNU sed extensions; BSD sed on macOS fails |
| ⏳ | [rpge](https://ftp.gnu.org/gnu/rpge/) | - |
| ✅ | [rush](https://ftp.gnu.org/gnu/rush/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=rush&expanded=true) |
| ⏳ | [sather](https://ftp.gnu.org/gnu/sather/) | - |
| 🚫 | [sauce](https://ftp.gnu.org/gnu/sauce/) | Not Supported: requires Tcl (tclsh) to build |
| ⏳ | [scm](https://ftp.gnu.org/gnu/scm/) | - |
| 🚫 | [screen](https://ftp.gnu.org/gnu/screen/) | Not Supported: requires ncurses on Linux; links libpam on macOS |
| ✅ | [sed](https://ftp.gnu.org/gnu/sed/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=sed&expanded=true) |
| 🚫 | [serveez](https://ftp.gnu.org/gnu/serveez/) | Not Supported: --without-guile unrecognized; guile required |
| 🚫 | [sharutils](https://ftp.gnu.org/gnu/sharutils/) | Not Supported: duplicate program_name symbol conflict |
| ⏳ | [shepherd](https://ftp.gnu.org/gnu/shepherd/) | - |
| ⏳ | [shishi](https://ftp.gnu.org/gnu/shishi/) | - |
| ✅ | [shtool](https://ftp.gnu.org/gnu/shtool/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=shtool&expanded=true) |
| ⏳ | [sipwitch](https://ftp.gnu.org/gnu/sipwitch/) | - |
| ⏳ | [slib](https://ftp.gnu.org/gnu/slib/) | - |
| ⏳ | [smalltalk](https://ftp.gnu.org/gnu/smalltalk/) | - |
| ⏳ | [solfege](https://ftp.gnu.org/gnu/solfege/) | - |
| ⏳ | [spacechart](https://ftp.gnu.org/gnu/spacechart/) | - |
| ✅ | [speedx](https://ftp.gnu.org/gnu/speedx/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=speedx&expanded=true) |
| ✅ | [spell](https://ftp.gnu.org/gnu/spell/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=spell&expanded=true) |
| ⏳ | [sqltutor](https://ftp.gnu.org/gnu/sqltutor/) | - |
| ⏳ | [src-highlite](https://ftp.gnu.org/gnu/src-highlite/) | - |
| ✅ | [stow](https://ftp.gnu.org/gnu/stow/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=stow&expanded=true) |
| 🚫 | [superopt](https://ftp.gnu.org/gnu/superopt/) | Not Supported: requires explicit CPU target flag; very old code |
| 🚫 | [swbis](https://ftp.gnu.org/gnu/swbis/) | Not Supported: old config.guess fails on macOS arm64; needs libz.a |
| ⏳ | [taler](https://ftp.gnu.org/gnu/taler/) | - |
| ✅ | [tar](https://ftp.gnu.org/gnu/tar/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=tar&expanded=true) |
| ⏳ | [termcap](https://ftp.gnu.org/gnu/termcap/) | - |
| 🚫 | [termutils](https://ftp.gnu.org/gnu/termutils/) | Not Supported: K&R C syntax errors on modern compilers |
| ✅ | [teseq](https://ftp.gnu.org/gnu/teseq/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=teseq&expanded=true) |
| ⏳ | [teximpatient](https://ftp.gnu.org/gnu/teximpatient/) | - |
| ✅ | [texinfo](https://ftp.gnu.org/gnu/texinfo/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=texinfo&expanded=true) |
| ✅ | [time](https://ftp.gnu.org/gnu/time/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=time&expanded=true) |
| ⏳ | [tramp](https://ftp.gnu.org/gnu/tramp/) | - |
| ⏳ | [trueprint](https://ftp.gnu.org/gnu/trueprint/) | - |
| ✅ | [units](https://ftp.gnu.org/gnu/units/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=units&expanded=true) |
| ✅ | [unrtf](https://ftp.gnu.org/gnu/unrtf/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=unrtf&expanded=true) |
| ✅ | [userv](https://ftp.gnu.org/gnu/userv/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=userv&expanded=true) |
| 🚫 | [uucp](https://ftp.gnu.org/gnu/uucp/) | Not Supported: 1994-era configure fails on macOS |
| ✅ | [vc-changelog](https://ftp.gnu.org/gnu/vc-changelog/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=vc-changelog&expanded=true) |
| ✅ | [vc-dwim](https://ftp.gnu.org/gnu/vc-dwim/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=vc-dwim&expanded=true) |
| 🚫 | [vcdimager](https://ftp.gnu.org/gnu/vcdimager/) | Not Supported: requires libcdio |
| 🚫 | [vera](https://ftp.gnu.org/gnu/vera/) | Not Supported: data-only package; no C binary |
| ⏳ | [wb](https://ftp.gnu.org/gnu/wb/) | - |
| ✅ | [wdiff](https://ftp.gnu.org/gnu/wdiff/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=wdiff&expanded=true) |
| ⏳ | [websocket4j](https://ftp.gnu.org/gnu/websocket4j/) | - |
| ✅ | [wget](https://ftp.gnu.org/gnu/wget/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=wget&expanded=true) |
| 🚫 | [which](https://ftp.gnu.org/gnu/which/) | Not Supported: getopt type conflict on macOS |
| ⏳ | [xaos](https://ftp.gnu.org/gnu/xaos/) | - |
| ⏳ | [xboard](https://ftp.gnu.org/gnu/xboard/) | - |
| ⏳ | [xlogmaster](https://ftp.gnu.org/gnu/xlogmaster/) | - |
| ⏳ | [xnee](https://ftp.gnu.org/gnu/xnee/) | - |
| 🚫 | [xorriso](https://ftp.gnu.org/gnu/xorriso/) | Not Supported: requires kernel headers + libbz2/libedit on macOS |
| ⏳ | [zile](https://ftp.gnu.org/gnu/zile/) | - |
