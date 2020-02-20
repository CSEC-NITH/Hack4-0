S
      }

      res.status(200).json(transfers);
   } catch (err) {
      passError(err, next);
   }
};

// Get single transfer
exports.getSingle = async (req, res, next) => {
   try {
      let transfer = await Transfer.findOne({
         _id: req.params.id,
         $or: [{ sender: req.user._id }, { recipient: req.user._id }]
      }).lean();

      if (!transfer) {
         throwError('No transfer found', 422);
      }

      res.status(200).json(transfer);
   } catch (err) {
      passError(err, next);
   }
};

// Create a new transfer
exports.create = async (req, res, next) => {
   const transfer = new Transfer(req.body);

   try {
      await transfer.save();

      if (!transfer) {
         throwError('Problems sending a transfer', 422);
      }

      res.status(201).json({ message: 'Transfer sent' });
   } catch (err) {
      passError(err, next);
   }
};
