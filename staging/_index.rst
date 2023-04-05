---
title: My Document Title
description: This is an example document that uses roles in reStructuredText.
---


Introduction
------------

This is an example document that uses roles in reStructuredText.

:emphasis:`Emphasis` can be added to text using the `emphasis` role.

:literal:`Code` can be highlighted using the `literal` role.

Links to other documents can be created using the `doc` role. For example, see the :doc:`link to another document`.

References to specific sections of a document can be created using the `ref` role. For example, see the :ref:`Introduction` section.

Conclusion
----------

That's it for this example document. Happy writing!


.. role:: doc
    :format: rst
    :parser: my_parser.parse_doc

.. role:: blah
    :class: a



:blah:`hello` 


.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.


.. role:: raw-role(raw)
   :format: html latex


:raw-role:`raw text`
