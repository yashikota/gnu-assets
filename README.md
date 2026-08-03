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
| 🚫 | [acm](https://ftp.gnu.org/gnu/acm/) | Not Supported: X11 flight simulator game, requires Xaw3D |
| ✅ | [adns](https://ftp.gnu.org/gnu/adns/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=adns&expanded=true) |
| 🚫 | [alive](https://ftp.gnu.org/gnu/alive/) | Not Supported: requires guile scripting engine |
| 🚫 | [anastasis](https://ftp.gnu.org/gnu/anastasis/) | Not Supported: requires libgcrypt/libcurl/complex deps |
| ✅ | [anubis](https://ftp.gnu.org/gnu/anubis/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=anubis&expanded=true) |
| 🚫 | [apl](https://ftp.gnu.org/gnu/apl/) | Not Supported: C++ APL interpreter, requires complex static build |
| 🚫 | [archimedes](https://ftp.gnu.org/gnu/archimedes/) | Not Supported: requires GSL, GTK, X11 |
| 🚫 | [aris](https://ftp.gnu.org/gnu/aris/) | Not Supported: GTK logic proof assistant, requires GTK |
| 🚫 | [artanis](https://ftp.gnu.org/gnu/artanis/) | Not Supported: Guile web framework, requires Guile |
| 🚫 | [aspell](https://ftp.gnu.org/gnu/aspell/) | Not Supported: libtool + C++ |
| 🚫 | [aspell-dict-csb](https://ftp.gnu.org/gnu/aspell-dict-csb/) | Not Supported: dictionary data files only, no CLI binary |
| 🚫 | [aspell-dict-ga](https://ftp.gnu.org/gnu/aspell-dict-ga/) | Not Supported: dictionary data files only, no CLI binary |
| 🚫 | [aspell-dict-hr](https://ftp.gnu.org/gnu/aspell-dict-hr/) | Not Supported: dictionary data files only, no CLI binary |
| 🚫 | [aspell-dict-is](https://ftp.gnu.org/gnu/aspell-dict-is/) | Not Supported: dictionary data files only, no CLI binary |
| 🚫 | [aspell-dict-it](https://ftp.gnu.org/gnu/aspell-dict-it/) | Not Supported: dictionary data files only, no CLI binary |
| 🚫 | [aspell-dict-sk](https://ftp.gnu.org/gnu/aspell-dict-sk/) | Not Supported: dictionary data files only, no CLI binary |
| 🚫 | [auctex](https://ftp.gnu.org/gnu/auctex/) | Not Supported: Emacs LaTeX package, no standalone CLI binary |
| 🚫 | [autoconf](https://ftp.gnu.org/gnu/autoconf/) | Not Supported: Perl scripts only, no C binary |
| 🚫 | [autoconf-archive](https://ftp.gnu.org/gnu/autoconf-archive/) | Not Supported: m4 macro collection, no CLI binary |
| 🚫 | [autogen](https://ftp.gnu.org/gnu/autogen/) | Not Supported: libtool + requires Guile |
| 🚫 | [automake](https://ftp.gnu.org/gnu/automake/) | Not Supported: Perl scripts only, no C binary |
| 🚫 | [avl](https://ftp.gnu.org/gnu/avl/) | Not Supported: GPG signature verification fails |
| 🚫 | [ballandpaddle](https://ftp.gnu.org/gnu/ballandpaddle/) | Not Supported: SDL game, requires SDL2 |
| 🚫 | [barcode](https://ftp.gnu.org/gnu/barcode/) | Not Supported: multiple definition bug in old code |
| ✅ | [bash](https://ftp.gnu.org/gnu/bash/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bash&expanded=true) |
| 🚫 | [bayonne](https://ftp.gnu.org/gnu/bayonne/) | Not Supported: C++ telephony server, requires uCommon/libtool |
| ✅ | [bc](https://ftp.gnu.org/gnu/bc/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bc&expanded=true) |
| 🚫 | [binutils](https://ftp.gnu.org/gnu/binutils/) | Not Supported: uses libtool internally; extremely complex build system |
| ✅ | [bison](https://ftp.gnu.org/gnu/bison/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bison&expanded=true) |
| ✅ | [bool](https://ftp.gnu.org/gnu/bool/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=bool&expanded=true) |
| 🚫 | [c-graph](https://ftp.gnu.org/gnu/c-graph/) | Not Supported: requires Fortran compiler |
| 🚫 | [c-intro-and-ref](https://ftp.gnu.org/gnu/c-intro-and-ref/) | Not Supported: documentation only, no CLI binary |
| 🚫 | [ccaudio](https://ftp.gnu.org/gnu/ccaudio/) | Not Supported: C++ audio library (libtool), no standalone CLI |
| 🚫 | [ccd2cue](https://ftp.gnu.org/gnu/ccd2cue/) | Not Supported: uses GNU error.h (glibc-only), not in musl |
| 🚫 | [ccrtp](https://ftp.gnu.org/gnu/ccrtp/) | Not Supported: C++ RTP library (libtool), no standalone CLI |
| 🚫 | [ccscript](https://ftp.gnu.org/gnu/ccscript/) | Not Supported: C++ scripting library (libtool), no standalone CLI |
| 🚫 | [cfengine](https://ftp.gnu.org/gnu/cfengine/) | Not Supported: requires OpenSSL + PCRE; complex static deps |
| 🚫 | [cflow](https://ftp.gnu.org/gnu/cflow/) | Not Supported: gnulib bitrotate.h uses [[maybe_unused]] via _GL_EXTERN_INLINE on return types; macOS clang rejects even in v1.8 |
| 🚫 | [cgicc](https://ftp.gnu.org/gnu/cgicc/) | Not Supported: C++ CGI library (libtool), no standalone CLI |
| ✅ | [chess](https://ftp.gnu.org/gnu/chess/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=chess&expanded=true) |
| 🚫 | [cim](https://ftp.gnu.org/gnu/cim/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [classpath](https://ftp.gnu.org/gnu/classpath/) | Not Supported: Java class library, no standalone CLI binary |
| 🚫 | [classpathx](https://ftp.gnu.org/gnu/classpathx/) | Not Supported: Java extensions for GNU Classpath, no CLI binary |
| 🚫 | [combine](https://ftp.gnu.org/gnu/combine/) | Not Supported: config.sub too old for macOS arm64 (missing CPU prefix in host triplet) |
| 🚫 | [commoncpp](https://ftp.gnu.org/gnu/commoncpp/) | Not Supported: C++ threading library (libtool), no standalone CLI |
| 🚫 | [complexity](https://ftp.gnu.org/gnu/complexity/) | Not Supported: requires libopts |
| ✅ | [coreutils](https://ftp.gnu.org/gnu/coreutils/) | - |
| ✅ | [cpio](https://ftp.gnu.org/gnu/cpio/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=cpio&expanded=true) |
| ✅ | [cppi](https://ftp.gnu.org/gnu/cppi/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=cppi&expanded=true) |
| ✅ | [cssc](https://ftp.gnu.org/gnu/cssc/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=cssc&expanded=true) |
| 🚫 | [cursynth](https://ftp.gnu.org/gnu/cursynth/) | Not Supported: requires ncurses + PortAudio |
| 🚫 | [dap](https://ftp.gnu.org/gnu/dap/) | Not Supported: libtool on Linux; uses finite() (non-standard) on macOS |
| ✅ | [datamash](https://ftp.gnu.org/gnu/datamash/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=datamash&expanded=true) |
| 🚫 | [ddd](https://ftp.gnu.org/gnu/ddd/) | Not Supported: graphical debugger, requires Motif/X11 |
| ✅ | [ddrescue](https://ftp.gnu.org/gnu/ddrescue/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=ddrescue&expanded=true) |
| 🚫 | [dejagnu](https://ftp.gnu.org/gnu/dejagnu/) | Not Supported: Tcl/Expect-based test framework, no C binary |
| 🚫 | [denemo](https://ftp.gnu.org/gnu/denemo/) | Not Supported: GTK music notation editor, requires GTK/MIDI |
| 🚫 | [dico](https://ftp.gnu.org/gnu/dico/) | Not Supported: libtool shared plugin modules; requires Guile |
| ✅ | [diction](https://ftp.gnu.org/gnu/diction/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=diction&expanded=true) |
| ✅ | [diffutils](https://ftp.gnu.org/gnu/diffutils/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=diffutils&expanded=true) |
| 🚫 | [direvent](https://ftp.gnu.org/gnu/direvent/) | Not Supported: macOS lacks clock_nanosleep / TIMER_ABSTIME |
| 🚫 | [dominion](https://ftp.gnu.org/gnu/dominion/) | Not Supported: requires ncurses |
| 🚫 | [easejs](https://ftp.gnu.org/gnu/easejs/) | Not Supported: JavaScript library, no CLI binary |
| ✅ | [ed](https://ftp.gnu.org/gnu/ed/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=ed&expanded=true) |
| 🚫 | [edma](https://ftp.gnu.org/gnu/edma/) | Not Supported: shell scripts only, no C binary |
| 🚫 | [electric](https://ftp.gnu.org/gnu/electric/) | Not Supported: Java VLSI CAD tool, requires Java runtime |
| 🚫 | [emacs](https://ftp.gnu.org/gnu/emacs/) | Not Supported: GUI text editor with complex deps (X11/GTK/GMP) |
| 🚫 | [emms](https://ftp.gnu.org/gnu/emms/) | Not Supported: Emacs music player package, not a standalone binary |
| ✅ | [enscript](https://ftp.gnu.org/gnu/enscript/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=enscript&expanded=true) |
| 🚫 | [fdisk](https://ftp.gnu.org/gnu/fdisk/) | Not Supported: requires GNU Parted (parted.h) |
| 🚫 | [ferret](https://ftp.gnu.org/gnu/ferret/) | Not Supported: no configure script; bare Makefile fails with musl-gcc |
| ✅ | [findutils](https://ftp.gnu.org/gnu/findutils/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=findutils&expanded=true) |
| 🚫 | [fisicalab](https://ftp.gnu.org/gnu/fisicalab/) | Not Supported: GTK physics lab, requires GTK |
| 🚫 | [foliot](https://ftp.gnu.org/gnu/foliot/) | Not Supported: Guile/GTK time tracking, requires Guile + GTK |
| 🚫 | [fontopia](https://ftp.gnu.org/gnu/fontopia/) | Not Supported: requires libncurses; console font editor |
| 🚫 | [fontutils](https://ftp.gnu.org/gnu/fontutils/) | Not Supported: old code (1992); no configure script, bare Makefile |
| 🚫 | [freedink](https://ftp.gnu.org/gnu/freedink/) | Not Supported: requires SDL2 and related libs |
| 🚫 | [freeipmi](https://ftp.gnu.org/gnu/freeipmi/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [freetalk](https://ftp.gnu.org/gnu/freetalk/) | Not Supported: Guile-based Jabber client, requires Guile/libgloox |
| 🚫 | [g-golf](https://ftp.gnu.org/gnu/g-golf/) | Not Supported: Guile GTK bindings, requires Guile + GLib |
| ✅ | [gama](https://ftp.gnu.org/gnu/gama/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gama&expanded=true) |
| ✅ | [gawk](https://ftp.gnu.org/gnu/gawk/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gawk&expanded=true) |
| ✅ | [gcal](https://ftp.gnu.org/gnu/gcal/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gcal&expanded=true) |
| 🚫 | [gcc](https://ftp.gnu.org/gnu/gcc/) | Not Supported: compiler toolchain, extremely complex build system |
| 🚫 | [gcide](https://ftp.gnu.org/gnu/gcide/) | Not Supported: dictionary database files only, no CLI binary |
| 🚫 | [gcl](https://ftp.gnu.org/gnu/gcl/) | Not Supported: GNU Common Lisp interpreter, requires GMP + complex build |
| 🚫 | [gcompris](https://ftp.gnu.org/gnu/gcompris/) | Not Supported: GTK educational game suite, requires GTK/SDL |
| 🚫 | [gdb](https://ftp.gnu.org/gnu/gdb/) | Not Supported: debugger, requires complex static linking |
| 🚫 | [gdbm](https://ftp.gnu.org/gnu/gdbm/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [gengen](https://ftp.gnu.org/gnu/gengen/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gengen&expanded=true) |
| 🚫 | [gengetopt](https://ftp.gnu.org/gnu/gengetopt/) | Not Supported: C++: musl-gcc has no static libstdc++ |
| 🚫 | [gettext](https://ftp.gnu.org/gnu/gettext/) | Not Supported: gnulib off64_t conflict with musl; macOS undefined symbols |
| 🚫 | [gforth](https://ftp.gnu.org/gnu/gforth/) | Not Supported: Forth interpreter, libtool shared libs |
| 🚫 | [ggradebook](https://ftp.gnu.org/gnu/ggradebook/) | Not Supported: GTK gradebook, requires GTK |
| 🚫 | [ghostscript](https://ftp.gnu.org/gnu/ghostscript/) | Not Supported: requires many external libs (X11, libpng, libjpeg, etc.) |
| 🚫 | [gift](https://ftp.gnu.org/gnu/gift/) | Not Supported: C++ image retrieval, libtool + complex deps |
| 🚫 | [git](https://ftp.gnu.org/gnu/git/) | Not Supported: not a GNU package; only a symlink/redirect on FTP |
| 🚫 | [global](https://ftp.gnu.org/gnu/global/) | Not Supported: libtool shared lib in plugin subdir |
| 🚫 | [glpk](https://ftp.gnu.org/gnu/glpk/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [gnats](https://ftp.gnu.org/gnu/gnats/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gnats&expanded=true) |
| 🚫 | [gnatsweb](https://ftp.gnu.org/gnu/gnatsweb/) | Not Supported: Perl web interface for GNATS, no C binary |
| 🚫 | [gnu-c-manual](https://ftp.gnu.org/gnu/gnu-c-manual/) | Not Supported: documentation only, no CLI binary |
| 🚫 | [gnu-crypto](https://ftp.gnu.org/gnu/gnu-crypto/) | Not Supported: Java cryptography library, no standalone CLI binary |
| 🚫 | [gnu-pw-mgr](https://ftp.gnu.org/gnu/gnu-pw-mgr/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [gnuastro](https://ftp.gnu.org/gnu/gnuastro/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [gnubatch](https://ftp.gnu.org/gnu/gnubatch/) | Not Supported: requires ncurses; musl-gcc cannot find headers |
| 🚫 | [gnubg](https://ftp.gnu.org/gnu/gnubg/) | Not Supported: GTK backgammon, requires GTK/Cairo |
| 🚫 | [gnubik](https://ftp.gnu.org/gnu/gnubik/) | Not Supported: GTK/OpenGL Rubik's cube, requires GTK/OpenGL |
| ✅ | [gnucap](https://ftp.gnu.org/gnu/gnucap/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gnucap&expanded=true) |
| 🚫 | [gnucobol](https://ftp.gnu.org/gnu/gnucobol/) | Not Supported: requires GMP and Berkeley DB |
| 🚫 | [gnudos](https://ftp.gnu.org/gnu/gnudos/) | Not Supported: requires ncurses; fcloseall (GNU-only) on macOS |
| ✅ | [gnugo](https://ftp.gnu.org/gnu/gnugo/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gnugo&expanded=true) |
| 🚫 | [gnuit](https://ftp.gnu.org/gnu/gnuit/) | Not Supported: requires ncurses |
| 🚫 | [gnujump](https://ftp.gnu.org/gnu/gnujump/) | Not Supported: SDL platform game, requires SDL |
| 🚫 | [gnukart](https://ftp.gnu.org/gnu/gnukart/) | Not Supported: not available on FTP (empty/removed project) |
| 🚫 | [gnumach](https://ftp.gnu.org/gnu/gnumach/) | Not Supported: Mach microkernel, not a CLI tool |
| 🚫 | [gnun](https://ftp.gnu.org/gnu/gnun/) | Not Supported: GNU web translation tool (make/shell scripts), no C binary |
| 🚫 | [gnunet](https://ftp.gnu.org/gnu/gnunet/) | Not Supported: requires libgcrypt/libgnutls/libcurl/complex deps |
| 🚫 | [gnupod](https://ftp.gnu.org/gnu/gnupod/) | Not Supported: Perl scripts only, no C binary |
| 🚫 | [gnuprologjava](https://ftp.gnu.org/gnu/gnuprologjava/) | Not Supported: Java Prolog interpreter, no standalone CLI binary |
| 🚫 | [gnuradio](https://ftp.gnu.org/gnu/gnuradio/) | Not Supported: requires FFTW/Boost/Python/Qt, extremely complex build |
| 🚫 | [gnurobots](https://ftp.gnu.org/gnu/gnurobots/) | Not Supported: GTK robot game, requires GTK/Guile |
| 🚫 | [gnuschool](https://ftp.gnu.org/gnu/gnuschool/) | Not Supported: PHP/web application, no CLI binary |
| ✅ | [gnushogi](https://ftp.gnu.org/gnu/gnushogi/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gnushogi&expanded=true) |
| 🚫 | [gnusound](https://ftp.gnu.org/gnu/gnusound/) | Not Supported: GTK audio editor, requires GTK/audio libs |
| 🚫 | [gnuspeech](https://ftp.gnu.org/gnu/gnuspeech/) | Not Supported: speech synthesis, requires complex audio/DSP libs |
| 🚫 | [gnuspool](https://ftp.gnu.org/gnu/gnuspool/) | Not Supported: requires ncurses + complex UNIX daemon setup |
| 🚫 | [gnutls](https://ftp.gnu.org/gnu/gnutls/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [gnutrition](https://ftp.gnu.org/gnu/gnutrition/) | Not Supported: GTK nutrition tracker, requires GTK3 |
| 🚫 | [goptical](https://ftp.gnu.org/gnu/goptical/) | Not Supported: C++ optical design library, no standalone CLI |
| 🚫 | [gperf](https://ftp.gnu.org/gnu/gperf/) | Not Supported: gnulib off64_t typedef conflict with musl |
| 🚫 | [gprofng-gui](https://ftp.gnu.org/gnu/gprofng-gui/) | Not Supported: Java GUI for gprofng, requires Java runtime |
| 🚫 | [gprolog](https://ftp.gnu.org/gnu/gprolog/) | Not Supported: configure is in src/ only; non-standard build system |
| 🚫 | [greg](https://ftp.gnu.org/gnu/greg/) | Not Supported: libtool; Guile/Tcl-based test framework |
| ✅ | [grep](https://ftp.gnu.org/gnu/grep/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=grep&expanded=true) |
| 🚫 | [groff](https://ftp.gnu.org/gnu/groff/) | Not Supported: gnulib off64_t conflict with musl |
| 🚫 | [grub](https://ftp.gnu.org/gnu/grub/) | Not Supported: bootloader, not a general CLI tool |
| 🚫 | [gsasl](https://ftp.gnu.org/gnu/gsasl/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [gsegrafix](https://ftp.gnu.org/gnu/gsegrafix/) | Not Supported: GTK scientific plotting, requires GTK |
| 🚫 | [gsrc](https://ftp.gnu.org/gnu/gsrc/) | Not Supported: GNU source repository (shell scripts), no C binary |
| 🚫 | [gss](https://ftp.gnu.org/gnu/gss/) | Not Supported: gnulib-generated stdint.h syntax error on musl/macOS |
| 🚫 | [gtypist](https://ftp.gnu.org/gnu/gtypist/) | Not Supported: requires ncursesw; musl-gcc cannot find headers |
| 🚫 | [guile](https://ftp.gnu.org/gnu/guile/) | Not Supported: Scheme interpreter, requires GMP/libgc/libtool |
| 🚫 | [guile-cv](https://ftp.gnu.org/gnu/guile-cv/) | Not Supported: Guile extension, requires Guile + Vignette |
| 🚫 | [guile-debbugs](https://ftp.gnu.org/gnu/guile-debbugs/) | Not Supported: Guile extension, no standalone CLI binary |
| 🚫 | [guile-gtk](https://ftp.gnu.org/gnu/guile-gtk/) | Not Supported: Guile GTK bindings, requires Guile + GTK |
| 🚫 | [guile-ncurses](https://ftp.gnu.org/gnu/guile-ncurses/) | Not Supported: Guile ncurses bindings, no standalone CLI binary |
| 🚫 | [guile-opengl](https://ftp.gnu.org/gnu/guile-opengl/) | Not Supported: Guile OpenGL bindings, no standalone CLI binary |
| 🚫 | [guile-rpc](https://ftp.gnu.org/gnu/guile-rpc/) | Not Supported: Guile RPC library, no standalone CLI binary |
| 🚫 | [guile-sdl](https://ftp.gnu.org/gnu/guile-sdl/) | Not Supported: Guile SDL bindings, no standalone CLI binary |
| 🚫 | [guix](https://ftp.gnu.org/gnu/guix/) | Not Supported: Guile-based package manager, requires Guile + complex build |
| 🚫 | [gv](https://ftp.gnu.org/gnu/gv/) | Not Supported: X11 PostScript/PDF viewer, requires X11 |
| 🚫 | [gvpe](https://ftp.gnu.org/gnu/gvpe/) | Not Supported: VPN daemon, requires OpenSSL |
| 🚫 | [gwl](https://ftp.gnu.org/gnu/gwl/) | Not Supported: Guile workflow language, requires Guile |
| 🚫 | [gxmessage](https://ftp.gnu.org/gnu/gxmessage/) | Not Supported: GTK message dialog, requires GTK |
| ✅ | [gzip](https://ftp.gnu.org/gnu/gzip/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=gzip&expanded=true) |
| 🚫 | [halifax](https://ftp.gnu.org/gnu/halifax/) | Not Supported: GTK fax application, requires GTK |
| 🚫 | [health](https://ftp.gnu.org/gnu/health/) | Not Supported: Python/Tryton medical management system, no C binary |
| ✅ | [hello](https://ftp.gnu.org/gnu/hello/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=hello&expanded=true) |
| ✅ | [help2man](https://ftp.gnu.org/gnu/help2man/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=help2man&expanded=true) |
| 🚫 | [hp2xx](https://ftp.gnu.org/gnu/hp2xx/) | Not Supported: requires X11 on Linux; old getopt.c on macOS |
| 🚫 | [httptunnel](https://ftp.gnu.org/gnu/httptunnel/) | Not Supported: ancient autoconf configure; C compiler test fails on macOS clang |
| 🚫 | [hurd](https://ftp.gnu.org/gnu/hurd/) | Not Supported: OS kernel/microkernel, not a CLI tool |
| 🚫 | [hyperbole](https://ftp.gnu.org/gnu/hyperbole/) | Not Supported: Emacs Lisp package, not a standalone binary |
| 🚫 | [idutils](https://ftp.gnu.org/gnu/idutils/) | Not Supported: gnulib _GL_WARN_ON_USE(gets) fails on musl (gets removed) |
| 🚫 | [ignuit](https://ftp.gnu.org/gnu/ignuit/) | Not Supported: GTK flashcard application, requires GTK |
| ✅ | [indent](https://ftp.gnu.org/gnu/indent/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=indent&expanded=true) |
| ✅ | [inetutils](https://ftp.gnu.org/gnu/inetutils/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=inetutils&expanded=true) |
| 🚫 | [jacal](https://ftp.gnu.org/gnu/jacal/) | Not Supported: Scheme/SCSH CAS system, requires Scheme interpreter |
| 🚫 | [jami](https://ftp.gnu.org/gnu/jami/) | Not Supported: VoIP/messaging app, requires Qt/WebRTC/complex deps |
| 🚫 | [jel](https://ftp.gnu.org/gnu/jel/) | Not Supported: Java expression library, no standalone CLI binary |
| 🚫 | [jtw](https://ftp.gnu.org/gnu/jtw/) | Not Supported: Java Training Wheels library, no standalone CLI binary |
| ✅ | [jwhois](https://ftp.gnu.org/gnu/jwhois/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=jwhois&expanded=true) |
| 🚫 | [kawa](https://ftp.gnu.org/gnu/kawa/) | Not Supported: JVM-based Scheme, requires Java runtime |
| 🚫 | [less](https://ftp.gnu.org/gnu/less/) | Not Supported: requires ncurses built with musl; two-stage build |
| 🚫 | [lightning](https://ftp.gnu.org/gnu/lightning/) | Not Supported: library only, no CLI binary |
| 🚫 | [liquidwar6](https://ftp.gnu.org/gnu/liquidwar6/) | Not Supported: SDL/OpenGL game, requires SDL/OpenGL/complex deps |
| 🚫 | [lsh](https://ftp.gnu.org/gnu/lsh/) | Not Supported: requires GMP and nettle |
| ✅ | [m4](https://ftp.gnu.org/gnu/m4/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=m4&expanded=true) |
| 🚫 | [macchanger](https://ftp.gnu.org/gnu/macchanger/) | Not Supported: Linux-only; caddr_t missing in musl |
| 🚫 | [mailman](https://ftp.gnu.org/gnu/mailman/) | Not Supported: Python-based mailing list manager, no C binary |
| 🚫 | [mailutils](https://ftp.gnu.org/gnu/mailutils/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [make](https://ftp.gnu.org/gnu/make/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=make&expanded=true) |
| 🚫 | [marst](https://ftp.gnu.org/gnu/marst/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [maverik](https://ftp.gnu.org/gnu/maverik/) | Not Supported: abandoned VR project (last release 1999), no configure |
| 🚫 | [mc](https://ftp.gnu.org/gnu/mc/) | Not Supported: requires ncurses or S-Lang |
| 🚫 | [mcron](https://ftp.gnu.org/gnu/mcron/) | Not Supported: requires guile scripting engine |
| 🚫 | [mcsim](https://ftp.gnu.org/gnu/mcsim/) | Not Supported: libtool + requires liblapack |
| 🚫 | [mes](https://ftp.gnu.org/gnu/mes/) | Not Supported: Scheme bootstrap system for GNU, not a general CLI tool |
| 🚫 | [metahtml](https://ftp.gnu.org/gnu/metahtml/) | Not Supported: old HTML scripting system, complex build system |
| 🚫 | [micron](https://ftp.gnu.org/gnu/micron/) | Not Supported: macOS missing HOST_NAME_MAX; runner.c missing signal.h |
| 🚫 | [mifluz](https://ftp.gnu.org/gnu/mifluz/) | Not Supported: requires Berkeley DB; macOS dbenv error |
| 🚫 | [mig](https://ftp.gnu.org/gnu/mig/) | Not Supported: cpu.sym requires mach/message.h (Mach kernel header) |
| 🚫 | [miscfiles](https://ftp.gnu.org/gnu/miscfiles/) | Not Supported: data files only (word lists, country codes), no CLI binary |
| 🚫 | [moe](https://ftp.gnu.org/gnu/moe/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [motti](https://ftp.gnu.org/gnu/motti/) | Not Supported: C++: not fully static with musl-gcc |
| ✅ | [mtools](https://ftp.gnu.org/gnu/mtools/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=mtools&expanded=true) |
| 🚫 | [nano](https://ftp.gnu.org/gnu/nano/) | Not Supported: requires ncurses (musl/ncurses static link issue) |
| ✅ | [ncurses](https://ftp.gnu.org/gnu/ncurses/) | - |
| ✅ | [nettle](https://ftp.gnu.org/gnu/nettle/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=nettle&expanded=true) |
| 🚫 | [ocrad](https://ftp.gnu.org/gnu/ocrad/) | Not Supported: requires libpng |
| 🚫 | [octave](https://ftp.gnu.org/gnu/octave/) | Not Supported: requires FFTW/LAPACK/Atlas/OpenBLAS/complex deps |
| 🚫 | [oleo](https://ftp.gnu.org/gnu/oleo/) | Not Supported: ncurses/X11 spreadsheet, requires ncurses |
| 🚫 | [orgadoc](https://ftp.gnu.org/gnu/orgadoc/) | Not Supported: requires libxml2 + ICU |
| 🚫 | [osip](https://ftp.gnu.org/gnu/osip/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [parallel](https://ftp.gnu.org/gnu/parallel/) | Not Supported: Perl scripts only, no C binary |
| 🚫 | [parted](https://ftp.gnu.org/gnu/parted/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [patch](https://ftp.gnu.org/gnu/patch/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=patch&expanded=true) |
| ✅ | [pem](https://ftp.gnu.org/gnu/pem/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=pem&expanded=true) |
| ✅ | [pexec](https://ftp.gnu.org/gnu/pexec/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=pexec&expanded=true) |
| 🚫 | [pies](https://ftp.gnu.org/gnu/pies/) | Not Supported: Linux daemon; macOS lacks CBAUD/SIGPWR |
| 🚫 | [plotutils](https://ftp.gnu.org/gnu/plotutils/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [poke](https://ftp.gnu.org/gnu/poke/) | Not Supported: requires Boehm GC |
| 🚫 | [proxyknife](https://ftp.gnu.org/gnu/proxyknife/) | Not Supported: broken old code (implicit decls, pod2man failures) |
| 🚫 | [pspp](https://ftp.gnu.org/gnu/pspp/) | Not Supported: requires libtool + GTK for GUI; complex deps |
| 🚫 | [psychosynth](https://ftp.gnu.org/gnu/psychosynth/) | Not Supported: C++ audio synthesizer, requires liblo/ALSA/SDL |
| 🚫 | [pth](https://ftp.gnu.org/gnu/pth/) | Not Supported: POSIX thread library only, no standalone CLI |
| 🚫 | [radius](https://ftp.gnu.org/gnu/radius/) | Not Supported: uses u_char (BSD type) unavailable in musl |
| ✅ | [rcs](https://ftp.gnu.org/gnu/rcs/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=rcs&expanded=true) |
| 🚫 | [readline](https://ftp.gnu.org/gnu/readline/) | Not Supported: input line editing library only, no CLI binary |
| 🚫 | [recutils](https://ftp.gnu.org/gnu/recutils/) | Not Supported: libtool: -rpath causes musl dynamic load |
| 🚫 | [reftex](https://ftp.gnu.org/gnu/reftex/) | Not Supported: Emacs Lisp package, not a standalone binary |
| 🚫 | [remotecontrol](https://ftp.gnu.org/gnu/remotecontrol/) | Not Supported: PHP web application, no CLI binary |
| 🚫 | [rottlog](https://ftp.gnu.org/gnu/rottlog/) | Not Supported: configure uses GNU sed extensions; BSD sed on macOS fails |
| 🚫 | [rpge](https://ftp.gnu.org/gnu/rpge/) | Not Supported: Guile/SDL RPG engine, requires Guile + SDL |
| ✅ | [rush](https://ftp.gnu.org/gnu/rush/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=rush&expanded=true) |
| 🚫 | [sather](https://ftp.gnu.org/gnu/sather/) | Not Supported: Sather language compiler/interpreter, requires Tk/X11 |
| 🚫 | [sauce](https://ftp.gnu.org/gnu/sauce/) | Not Supported: requires Tcl (tclsh) to build |
| 🚫 | [scm](https://ftp.gnu.org/gnu/scm/) | Not Supported: Scheme interpreter, requires complex static deps |
| 🚫 | [screen](https://ftp.gnu.org/gnu/screen/) | Not Supported: requires ncurses on Linux; links libpam on macOS |
| ✅ | [sed](https://ftp.gnu.org/gnu/sed/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=sed&expanded=true) |
| 🚫 | [serveez](https://ftp.gnu.org/gnu/serveez/) | Not Supported: --without-guile unrecognized; guile required |
| 🚫 | [sharutils](https://ftp.gnu.org/gnu/sharutils/) | Not Supported: multiple definition of program_name (chdir-long.c in libgnu.a vs autogen opts code) |
| 🚫 | [shepherd](https://ftp.gnu.org/gnu/shepherd/) | Not Supported: Guile-based service manager, requires Guile |
| 🚫 | [shishi](https://ftp.gnu.org/gnu/shishi/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [shtool](https://ftp.gnu.org/gnu/shtool/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=shtool&expanded=true) |
| 🚫 | [sipwitch](https://ftp.gnu.org/gnu/sipwitch/) | Not Supported: libtool + requires uCommon/OpenSSL |
| 🚫 | [slib](https://ftp.gnu.org/gnu/slib/) | Not Supported: Scheme library, no standalone CLI binary |
| 🚫 | [smalltalk](https://ftp.gnu.org/gnu/smalltalk/) | Not Supported: Smalltalk interpreter, libtool + complex deps |
| 🚫 | [solfege](https://ftp.gnu.org/gnu/solfege/) | Not Supported: GTK music ear training, requires GTK/Python |
| 🚫 | [spacechart](https://ftp.gnu.org/gnu/spacechart/) | Not Supported: GTK/GL 3D star map, requires GTK/OpenGL |
| ✅ | [speedx](https://ftp.gnu.org/gnu/speedx/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=speedx&expanded=true) |
| ✅ | [spell](https://ftp.gnu.org/gnu/spell/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=spell&expanded=true) |
| 🚫 | [sqltutor](https://ftp.gnu.org/gnu/sqltutor/) | Not Supported: C++ CGI, requires PostgreSQL (libpqxx) |
| 🚫 | [src-highlite](https://ftp.gnu.org/gnu/src-highlite/) | Not Supported: libtool + requires Boost::regex |
| ✅ | [stow](https://ftp.gnu.org/gnu/stow/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=stow&expanded=true) |
| 🚫 | [superopt](https://ftp.gnu.org/gnu/superopt/) | Not Supported: requires explicit CPU target flag; very old code |
| 🚫 | [swbis](https://ftp.gnu.org/gnu/swbis/) | Not Supported: old config.guess fails on macOS arm64; needs libz.a |
| 🚫 | [taler](https://ftp.gnu.org/gnu/taler/) | Not Supported: GTK digital payment app, requires GTK/libgcrypt |
| ✅ | [tar](https://ftp.gnu.org/gnu/tar/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=tar&expanded=true) |
| 🚫 | [termcap](https://ftp.gnu.org/gnu/termcap/) | Not Supported: terminal capability library only, no CLI binary |
| 🚫 | [termutils](https://ftp.gnu.org/gnu/termutils/) | Not Supported: K&R C syntax errors on modern compilers |
| ✅ | [teseq](https://ftp.gnu.org/gnu/teseq/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=teseq&expanded=true) |
| 🚫 | [teximpatient](https://ftp.gnu.org/gnu/teximpatient/) | Not Supported: TeX book (documentation), no CLI binary |
| ✅ | [texinfo](https://ftp.gnu.org/gnu/texinfo/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=texinfo&expanded=true) |
| ✅ | [time](https://ftp.gnu.org/gnu/time/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=time&expanded=true) |
| 🚫 | [tramp](https://ftp.gnu.org/gnu/tramp/) | Not Supported: Emacs Lisp package (remote file editing), not standalone |
| 🚫 | [trueprint](https://ftp.gnu.org/gnu/trueprint/) | Not Supported: libtool: -rpath causes musl dynamic load |
| ✅ | [units](https://ftp.gnu.org/gnu/units/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=units&expanded=true) |
| ✅ | [unrtf](https://ftp.gnu.org/gnu/unrtf/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=unrtf&expanded=true) |
| ✅ | [userv](https://ftp.gnu.org/gnu/userv/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=userv&expanded=true) |
| 🚫 | [uucp](https://ftp.gnu.org/gnu/uucp/) | Not Supported: 1994-era configure fails on macOS |
| ✅ | [vc-changelog](https://ftp.gnu.org/gnu/vc-changelog/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=vc-changelog&expanded=true) |
| ✅ | [vc-dwim](https://ftp.gnu.org/gnu/vc-dwim/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=vc-dwim&expanded=true) |
| 🚫 | [vcdimager](https://ftp.gnu.org/gnu/vcdimager/) | Not Supported: requires libcdio |
| 🚫 | [vera](https://ftp.gnu.org/gnu/vera/) | Not Supported: data-only package; no C binary |
| 🚫 | [wb](https://ftp.gnu.org/gnu/wb/) | Not Supported: Scheme/Java database library, no C binary |
| ✅ | [wdiff](https://ftp.gnu.org/gnu/wdiff/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=wdiff&expanded=true) |
| 🚫 | [websocket4j](https://ftp.gnu.org/gnu/websocket4j/) | Not Supported: Java WebSocket library, no standalone CLI binary |
| ✅ | [wget](https://ftp.gnu.org/gnu/wget/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=wget&expanded=true) |
| ✅ | [which](https://ftp.gnu.org/gnu/which/) | [releases](https://github.com/yashikota/gnu-assets/releases?q=which&expanded=true) |
| 🚫 | [xaos](https://ftp.gnu.org/gnu/xaos/) | Not Supported: interactive fractal zoom, requires SDL2/GTK |
| 🚫 | [xboard](https://ftp.gnu.org/gnu/xboard/) | Not Supported: X11 chess board GUI, requires X11/Cairo |
| 🚫 | [xlogmaster](https://ftp.gnu.org/gnu/xlogmaster/) | Not Supported: GTK log monitor, requires GTK |
| 🚫 | [xnee](https://ftp.gnu.org/gnu/xnee/) | Not Supported: X11 event recorder, requires X11 |
| 🚫 | [xorriso](https://ftp.gnu.org/gnu/xorriso/) | Not Supported: requires kernel headers + libbz2/libedit on macOS |
| 🚫 | [zile](https://ftp.gnu.org/gnu/zile/) | Not Supported: requires curses library |
