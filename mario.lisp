#!/usr/bin/env sbcl --script
;; (ql:quickload :iterate)
;; (use-package :iterate)

(defun drawMountain (size block)
  (loop for i from 1 to size
                        collect (format t "~A" block))
  )

(let ((block "#")) (drawMountain 10 block))
