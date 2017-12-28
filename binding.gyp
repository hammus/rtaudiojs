{
    "include_dirs": [
        "lib/rtaudio",
        "lib/rtaudio/include"
    ],
    'conditions': [
        ['OS=="win"', {

            "targets": [{
                'target_name': 'RTAJSDS',  # RtAudioJs using MS DirectSound API
                'defines': ['__WINDOWS_DS__'],
                'link_settings': {
                    'libraries': ['-lole32', '-lwinmm', '-ldsound', '-luser32']
                },
                "sources": [
                    "RtAudioJS.cc",
                    "lib/rtaudio/RtAudio.cpp"
                ],
                'cflags!': ['-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions'],
                'configurations': {
                    'Release': {
                        'VCCLCompilerTool': {
                            'ExceptionHandling': '1',
                            'AdditionalOptions': ['/EHsc']
                        }
                    }
                }


            }, {
                'target_name': 'RTAJSWASAPI',  # RtAudioJs using WASAPI
                'defines': ['__WINDOWS_WASAPI__'],
                'link_settings': {
                    'libraries': ['-lole32', '-lwinmm', '-lksuser', '-luuid']
                },
                "sources": [
                    "RtAudioJS.cc",
                    "lib/rtaudio/RtAudio.cpp"
                ],
                'cflags': ['/EHsc'],
                'cflags_cc!': ['-fno-exceptions'],
                'configurations': {
                    'Release': {
                        'msvs_settings': {
                            'VCCLCompilerTool': {
                                'ExceptionHandling': '1',
                                'AdditionalOptions': ['/EHsc']
                            }
                        }
                    }
                }
            }]
        }]
    ]
}
